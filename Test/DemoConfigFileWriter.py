import pickle


d = {'run_interval_seconds': 3,
     "script_file_path": "C:/Users/ohadv/PycharmProjects/siemplify-exercise/VirusTotalConnector.py",
     "connector_name": 'Virus Total Domain Scanner',
     "output_folder_path": "C:/Users/ohadv/PycharmProjects/siemplify-exercise/output",
     "source_folder_path": "src1/domains_1.txt",
     "iteration_entities_count": 4}

geeky_file = open('config1.txt', 'wb')
pickle.dump(d,geeky_file)
geeky_file.close()


# read_file = open('config1.txt', 'rb')
# data = read_file.read()
# data = pickle.loads(data)
# print(data)
