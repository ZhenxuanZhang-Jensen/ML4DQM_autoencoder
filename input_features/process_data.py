'''
refer to Deep learning for certification of the quality of the data acquired by the CMS Experiment

```jsx
chrome-extension://kdpelmjpfafjppnhbloffcjpeomlnpah/file:///Users/zhenxuanzhang/Downloads/ML4DQM/Alan_Pol_2020_J._Phys.%20_Conf._Ser._1525_012045.pdf
```

they used `AOD dataset`, and the input features list should be https://github.com/AdrianAlan/Data-Certification/blob/master/feature_names.txt
'''

import subprocess
import subprocess
import yaml


class AOD:
    def __init__(self):
        pass

    def get_AOD_files(self):
        command = 'dasgoclient -query="file dataset=/DoubleEG/Run2016B-07Aug17_ver1-v1/AOD"'
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        output_name = 'AOD.yaml'
        template = "AOD:\n"

        for line in output.split('\n')[0:-1]:
            template += f"- {line}\n"

        # Save template as a text file
        with open('template.txt', 'w') as file:
            file.write(template)

        # Change the text file to a YAML file
        with open('template.txt', 'r') as file:
            data = file.read()
            yaml_data = yaml.safe_load(data)

        with open(output_name, 'w') as file:
            yaml.dump(yaml_data, file)

        # Debug print statements
        print("Output:", output)
        print("Template:", template)
        print("YAML Data:", yaml_data)


class TrainingDataProcessing:
    def __init__(self):
        pass

    def process_data(self):
        pass
    
    
if __name__ == "__main__":
    pass