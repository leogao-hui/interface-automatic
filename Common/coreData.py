# author:LEO GAO
# project Encoding:UTF-8


class CoreData:

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
        "surveyItem[preConditionItems][0][matchExp]": "身高>100",
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
        "surveyItem[preConditionItems][0][matchExp]": "(职业$1(休养或退休))",
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
        "surveyItem[preConditionItems][0][matchExp]": "(职业$1(专业技术人员))|(瘤种$1(肺癌,大肠癌))",
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
    }

    calculation_variable_one_data = {
        'name': '计算变量一',
        'optionalValues[0][matchExpression]': '职业$1(休养或退休)',
        'optionalValues[0][content]': '身高+20',
        'optionalValues[0][priority]': 1,
        'optionalValues[0][comment]': 'aaa',
        'comment': 'aaa',
        'isSolutionCanUse': 'yes'
    }

    calculation_variable_two_data = {
        'name': '计算变量二',
        'optionalValues[0][matchExpression]': '$$1((治疗阶段$1(姑息治疗期间,化疗期间)),瘤种$1(肺癌,大肠癌),(计算变量一>100))',
        'optionalValues[0][content]': '0',
        'optionalValues[0][priority]': 1,
        'optionalValues[0][comment]': '111',
        'comment': '111',
        'isSolutionCanUse': 'yes'
    }

    scale_variable_one_data = {
        'name': '量表变量',
        'optionalValues[0][matchExpression]': '*',
        'optionalValues[0][calcuRule]': 'sum',
        'optionalValues[0][rDirectVars][0][variableName]': '身高',
        'optionalValues[0][rDirectVars][0][valueCalcuRule]': 'max',
        'optionalValues[0][rDirectVars][0][comment]': 'aaaa',
        'optionalValues[0][rDirectVars][0][scoreItems][0][matchExp]': '身高=50',
        'optionalValues[0][rDirectVars][0][scoreItems][0][score]': 20,
        'comment': 'aaa',
        'isSolutionCanUse': 'yes'
    }

    information_structure_one_data = {
        'name': '信息结构1',
        'type': 'info',
        'content': '{"评估显示名": "val", "评估条件": "val", "评估意义": "val", "匹配结果项列表": "val"}',
        'sort': 1,
        'comment': ''
    }

    information_structure_two_data = {
        'name': '信息结构2',
        'type': 'info',
        'content': '{"定义": "val", "产生原因": "val", "微观影响说明": "val"}',
        'sort': 2,
        'comment': ''
    }

    root_template_data = {
        'name': '测试根模板',
        'type': 'evaluation_item',
        'displayTpl': '1111',
        'rootTpl': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"val","评估条件":"val",'
                   '"评估意义":"val","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},'
                   '"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                   '"content":[{"表达式":"expression","情况说明":"val","备注":"val"}]},'
                   '"匹配用结果项名":"val","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},'
                   '"content":{"定义":"val","产生原因":"val","微观影响说明":"val"}},"分组":"val","备注":"val"}]}}}',
        'comment': ''
    }

    evaluate_one_data = {
        'templateId': 1,
        'tags[0][name]': '标签一',
        'tags[1][name]': '标签二',
        'rank': 1,
        'name': '测试评估名1',
        'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名1","评估条件":"计算变量一>100","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                   '"content":[{"表达式":"(职业$1(休养或退休))","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
        'isSolutionCanUse': 'yes',
        'comment': '111'
    }

    evaluate_two_data = {
        'templateId': 1,
        'tags[0][name]': '标签一',
        'tags[1][name]': '标签二',
        'rank': 2,
        'name': '测试评估名2',
        'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名2","评估条件":"","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                   '"content":[{"表达式":"$$3((职业$1(休养或退休)),瘤种$1(肺癌,前列腺癌),(测试评估名1=匹配用结果项名1))","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
        'isSolutionCanUse': 'yes',
        'comment': '111'
    }

    evaluate_three_data = {
        'templateId': 1,
        'tags[0][name]': '标签一',
        'tags[1][name]': '标签二',
        'rank': 3,
        'name': '测试评估名3',
        'content': '{"info":{"id":1,"name":"信息结构1","type":"info"},"content":{"评估显示名":"评估显示名3","评估条件":"","评估意义":"1111","匹配结果项列表":{"info":{"id":-2,"name":"评估匹配结构","type":"evl_match"},"content":[{"适用条件":{"info":{"id":-2,"name":"表达式结构","type":"condition"},'
                   '"content":[{"表达式":"$$2((职业$1(休养或退休)),瘤种$1(肺癌,前列腺癌),(测试评估名1=匹配用结果项名1))","情况说明":"11","备注":"1"}]},"匹配用结果项名":"匹配用结果项名1","解读":{"info":{"id":2,"name":"信息结构2","type":"info"},"content":{"定义":"1","产生原因":"1","微观影响说明":"1"}},"分组":"1","备注":"1"}]},"用户可见结果项":{"info":{"id":-3,"name":"用户可见结果项","type":"visual"},"content":[{"适用条件表达式":"","用户可见的结果项名":"","分组":"","备注":""}]}}}',
        'isSolutionCanUse': 'yes',
        'comment': '111'
    }

    evaluate_version_one_data = {
        'name': '测试答题评估版本',
        'items[0][itemId]': 1,
        'items[0][itemType]': 'direct_variable',
        'items[1][itemId]': 2,
        'items[1][itemType]': 'direct_variable',
        'items[2][itemId]': 3,
        'items[2][itemType]': 'direct_variable',
        'items[3][itemId]': 4,
        'items[3][itemType]': 'direct_variable',
        'items[4][itemId]': 5,
        'items[4][itemType]': 'direct_variable',
        'items[5][itemId]': 1,
        'items[5][itemType]': 'calcu_variable',
        'items[6][itemId]': 2,
        'items[6][itemType]': 'calcu_variable',
        'items[7][itemId]': 1,
        'items[7][itemType]': 'evaluate_item',
    }

    combo_data = {
        'name': '测试答题套餐名',
        'evId': 1,
        'items[0][itemId]': 1,
        'items[0][itemType]': 'direct_variable',
        'items[1][itemId]': 2,
        'items[1][itemType]': 'direct_variable',
        'items[2][itemId]': 3,
        'items[2][itemType]': 'direct_variable',
        'items[3][itemId]': 4,
        'items[3][itemType]': 'direct_variable',
        'items[4][itemId]': 5,
        'items[4][itemType]': 'direct_variable',
        'items[5][itemId]': 1,
        'items[5][itemType]': 'calcu_variable',
        'items[6][itemId]': 2,
        'items[6][itemType]': 'calcu_variable',
        'items[7][itemId]': 1,
        'items[7][itemType]': 'evaluate_item',
    }

    team_data = {
        'name': '测试团队'
    }

    team_member_one_data = {
        'phone': '14342432424',
        'password': 'MTIzNDU2',
        'name': '123456',
        'belongTeamId': 1,
        'identity': 'manager'
    }

    filling_data = {
        'clerkId': 1,
        'comboId': 1,
        'name': '测试人',
        'phone': '13342423242',
        'sex': '男',
        'birthAt': '456',
        'representor': 'adadd',
        'nation': 'qdw',
        'address': 'dwdq',
        'caregiver': 'dwq',
        'caregiverPhone': 'dwdqdwd'
    }









