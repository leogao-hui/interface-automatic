# author:LEO GAO
# project Encoding:UTF-8


class manyData:

    height_data = {
        "variableName": "身高",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少",
        "surveyItem[rank]": "100",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
    }

    job_data = {
        "variableName": "职业",
        "variableValueType": "text",
        "optionalValues[0][variableValue]": "休养或退休",
        "optionalValues[0][sort]": "1",
        "optionalValues[1][variableValue]": "专业技术人员",
        "optionalValues[1][sort]": "2",
        "optionalValues[2][variableValue]": "行政办公人员",
        "optionalValues[2][sort]": "3",
        "optionalValues[3][variableValue]": "服务业人员",
        "optionalValues[3][sort]": "4",
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的职业是？",
        "surveyItem[rank]": "90",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "multiple_choice",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "comment",
        "surveyItem[options][0][surveyItemValue]": "休养或退休",
        "surveyItem[options][0][sort]": "1",
        "surveyItem[options][1][surveyItemValue]": "专业技术人员",
        "surveyItem[options][1][sort]": "2",
        "surveyItem[options][2][surveyItemValue]": "行政办公人员",
        "surveyItem[options][2][sort]": "3",
        "surveyItem[options][3][surveyItemValue]": "服务业人员",
        "surveyItem[options][3][sort]": "4",
        "surveyItem[preConditionItems][0][matchExp]": "身高>140",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",

    }

    tumor_data = {
        "variableName": "瘤种",
        "variableValueType": "text",
        "optionalValues[0][variableValue]": "肺癌",
        "optionalValues[0][sort]": "1",
        "optionalValues[1][variableValue]": "大肠癌",
        "optionalValues[1][sort]": "2",
        "optionalValues[2][variableValue]": "乳腺癌",
        "optionalValues[2][sort]": "3",
        "optionalValues[3][variableValue]": "前列腺癌",
        "optionalValues[3][sort]": "4",
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您得过什么瘤种？",
        "surveyItem[rank]": "80",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "multiple_choice",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "comment",
        "surveyItem[options][0][surveyItemValue]": "肺癌",
        "surveyItem[options][0][sort]": "1",
        "surveyItem[options][1][surveyItemValue]": "大肠癌",
        "surveyItem[options][1][sort]": "2",
        "surveyItem[options][2][surveyItemValue]": "乳腺癌",
        "surveyItem[options][2][sort]": "3",
        "surveyItem[options][3][surveyItemValue]": "前列腺癌",
        "surveyItem[options][3][sort]": "4",
        "surveyItem[preConditionItems][0][matchExp]": "身高>130",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111"
    }

    treatment_stage_data = {
        "variableName": "治疗阶段",
        "variableValueType": "text",
        "optionalValues[0][variableValue]": "姑息治疗期间",
        "optionalValues[0][sort]": "1",
        "optionalValues[1][variableValue]": "围手术期术后",
        "optionalValues[1][sort]": "2",
        "optionalValues[2][variableValue]": "化疗期间",
        "optionalValues[2][sort]": "3",
        "optionalValues[3][variableValue]": "放疗期间",
        "optionalValues[3][sort]": "4",
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您所处什么治疗阶段？",
        "surveyItem[rank]": "70",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "multiple_choice",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "comment",
        "surveyItem[options][0][surveyItemValue]": "姑息治疗期间",
        "surveyItem[options][0][sort]": "1",
        "surveyItem[options][1][surveyItemValue]": "围手术期术后",
        "surveyItem[options][1][sort]": "2",
        "surveyItem[options][2][surveyItemValue]": "乳腺癌",
        "surveyItem[options][2][sort]": "3",
        "surveyItem[options][3][surveyItemValue]": "前列腺癌",
        "surveyItem[options][3][sort]": "4",
        "surveyItem[preConditionItems][0][matchExp]": "身高>120",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    hobby_data = {
        "variableName": "兴趣爱好",
        "variableValueType": "text",
        "optionalValues[0][variableValue]": 1,
        "optionalValues[0][sort]": "1",
        "optionalValues[1][variableValue]": 2,
        "optionalValues[1][sort]": "2",
        "optionalValues[2][variableValue]": 3,
        "optionalValues[2][sort]": "3",
        "optionalValues[3][variableValue]": 4,
        "optionalValues[3][sort]": "4",
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的兴趣爱好是什么？",
        "surveyItem[rank]": "60",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "single_choice",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "comment",
        "surveyItem[options][0][surveyItemValue]": "没有减少",
        "surveyItem[options][0][sort]": "1",
        "surveyItem[options][1][surveyItemValue]": "略微减少参与次数",
        "surveyItem[options][1][sort]": "2",
        "surveyItem[options][2][surveyItemValue]": "明显减少",
        "surveyItem[options][2][sort]": "3",
        "surveyItem[options][3][surveyItemValue]": "基本不参与",
        "surveyItem[options][3][sort]": "4",
        "surveyItem[preConditionItems][0][matchExp]": "身高>110",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_1 = {
        "variableName": "身高1",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少1",
        "surveyItem[rank]": "50",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1000",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_2 = {
        "variableName": "身高11",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少11",
        "surveyItem[rank]": "40",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1001",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_3 = {
        "variableName": "身高11",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少11",
        "surveyItem[rank]": "40",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1002",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_4 = {
        "variableName": "身高111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少111",
        "surveyItem[rank]": "30",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1003",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_5 = {
        "variableName": "身高1111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少1111",
        "surveyItem[rank]": "20",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1004",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_6 = {
        "variableName": "身高11111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少11111",
        "surveyItem[rank]": "10",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1005",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_7 = {
        "variableName": "身高111111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少111111",
        "surveyItem[rank]": "9",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1006",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_8 = {
        "variableName": "身高1111111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少1111111",
        "surveyItem[rank]": "8",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1007",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_9 = {
        "variableName": "身高11111111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少11111111",
        "surveyItem[rank]": "7",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1008",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_10 = {
        "variableName": "身高111111111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少111111111",
        "surveyItem[rank]": "6",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高>1009",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }

    height_data_11 = {
        "variableName": "身高1111111111",
        "variableValueType": "numerical",
        "optionalValueMin": 20,
        "optionalValueMax": 250,
        "isSolutionCanUse": "yes",
        "surveyItem[title]": "您的身高是多少1111111111",
        "surveyItem[rank]": "5",
        "surveyItem[topicId]": "1",
        "surveyItem[type]": "fillup",
        "surveyItem[canRefuse]": "can_refuse",
        "surveyItem[device]": "device",
        "surveyItem[comment]": "",
        "surveyItem[preConditionItems][0][matchExp]": "身高<60",
        "surveyItem[preConditionItems][0][description]": "显示条件",
        "surveyItem[preConditionItems][0][comment]": "1111",
    }