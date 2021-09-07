from DataModels import ConnectorParams
from DataModels import ConnectorResult


class SubProcessInputOutputHandler(object):

    @property
    def connector_params(self):
        params = ConnectorParams()  # get the connector inputed parameters.

        # TODO: parse stdin input into ConnectorParams object and return it with populated values
        params.source_file_path = "src1/domains_1.txt"
        params.iteration_count = 1

        return params

    def end(self, connector_result):
        result = ConnectorResult()
        result.alerts = connector_result

        """ connector_result is of type ConnectorResult"""
        # TODO - pass connector result as stdout
        # TODO - end current process
