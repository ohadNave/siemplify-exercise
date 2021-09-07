import requests
import sys
import pickle
import base64
import datetime
import subprocess
import  json

from Exceptions.ConnectorException import ConnectorException
from SubProcessInputOutputHandler import SubProcessInputOutputHandler

API_KEY = "a5b799dc764cb0c0c3929a1986f631e772c3fa2aed026bd5463b0693c0943906"
url = "https://www.virustotal.com/api/v3/domains/{}"




def main():

    io_mgr = SubProcessInputOutputHandler()
    conn_params = io_mgr.connector_params
    entities_count = conn_params.iteration_entities_count

    # Read domains from src file.
    with open(conn_params.source_file_path) as input_file:
        connector_result = {}
        for i, domain_name in enumerate(input_file):
            if i == entities_count: break
            try:
                responseJSON = requests.get(url.format(domain_name), headers={'x-apikey': API_KEY}).json()
                connector_result[domain_name.rstrip()] = handle_domain_data(responseJSON['data']['attributes'])

            except KeyError:
                raise ConnectorException(responseJSON['error']['message'])

    # Write domains fetched data to an external file.
    with open("output/{}.txt".format(get_current_ts()), 'w') as output_file:
        for domain_name, result in connector_result.items():
            output_file.write('%s:%s\n' % (domain_name, result))


    io_mgr.end(connector_result)


def handle_domain_data(domain_data):
    extracted_domain_data = {}
    extracted_domain_data['decision'] = "Not Suspicious" if domain_data['reputation'] > 0 else "Suspicious"  # -100(fully malicious) to 100(fully harmless)
    extracted_domain_data['total_votes'] = domain_data['total_votes']
    return extracted_domain_data

def get_current_ts():
    return datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')


if __name__ == "__main__":
    main()
# TODO Implement Connector Logic
