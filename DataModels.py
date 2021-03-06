

class ConnectorSettings(object):
    run_interval_seconds = None  # int - iterations interval in seconds for current connector
    script_file_path = None  # string - the file path to the connector script
    connector_name = 'Virus Total Domain Scanner'  # string - connector name
    params = None  # ConnectorParams object - see below
    output_folder_path = "C:/Users/ohadv/PycharmProjects/siemplify-exercise/output" # string - file path for connector output


class ConnectorParams(object):
    source_folder_path = ""  # string - file path for entity list files
    iteration_entities_count = 3  # int - how many entities to process each interval (ignore the rest)


class ConnectorResult(object):
    alerts = None  # Dictionary {string, any} - connector output with data per entity. Key = Entity, value = entity data
