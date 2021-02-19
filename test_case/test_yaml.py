import yaml

#safe_load将yaml文件的数据流转换成python对象
# safe_dump将python对象转行成yaml格式

def test_yaml():
    with open("../test_data/test_yaml_data.yml",encoding='gb18030', errors='ignore') as f:
        test_data = yaml.safe_load(f)
        print(test_data)