# author:LEO GAO
# project Encoding:UTF-8


import logging
import configparser
import os

first = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
case_path = os.path.join(first, "config.ini")
config = configparser.ConfigParser()
config.read(case_path)


ci_url_1 = config.get("url", "backend_url")
ci_url = ci_url_1[1:-1]


# 新增直接变量
add_direct_variable_url_ci = '%s/api/rule/directVariable' % ci_url

# 新增计算变量
add_calculation_variable_url_ci = '%s/api/rule/calcuVariable' % ci_url

# 新增量表变量
add_scale_variable_url_ci = '%s/api/rule/scaleVariable' % ci_url

# 新增显示变量
add_display_variable_url_ci = '%s/api/rule/displayVariable' % ci_url

# 获取系统变量
get_system_variable_url_ci = '%s/api/rule/systemVariable' % ci_url

# 新增信息结构
add_information_structure_url_ci = '%s/api/rule/structure' % ci_url

# 新增根模板URL
add_root_template_url_ci = '%s/api/rule/rootTpl' % ci_url

# 新增评估项URL
add_evaluate_url_ci = '%s/api/rule/evaluateItem' % ci_url

# 新增评估版本URL
add_evaluate_version_url_ci = '%s/api/rule/evVersion' % ci_url

# 新增套餐
add_combo_url_ci = '%s/api/rule/combo' % ci_url

# 新增团队
add_team_url_ci = '%s/api/collection/team' % ci_url

# 新增团队人员
add_team_member_url_ci = '%s/api/collection/clerk' % ci_url

# 新增建档
add_filling_url_ci = '%s/api/collection/patient' % ci_url

# 新增食材
add_food_url_ci = '%s/api/rule/foodMaterial' % ci_url

# 新增食材库
add_food_label_library_url_ci = '%s/api/rule/foodMaterialTag' % ci_url

# 新增食材应用场景库
add_food_application_scene_library_url_ci = '%s/api/rule/foodMaterialApplyScenario' % ci_url

# 提交题目
submit_question_url_ci = '%s/api/collection/patientSurveyResultItem' % ci_url

# 获取下一题
# receive_next_question_url_ci = '%s/api/collection/patientSurveyResult/%s/nextSurveyItem' % ci_url

# 生成方案
generate_solution_url_ci = '%s/api/production/patientSolution/regenerate' % ci_url

# 生成报告
generate_report_url_ci = '%s/api/production/report/evaluationResult/regenerate' % ci_url

# 测试数据构造
generate_evaluation_data_url_ci = '%s/api/tool/generateEvaluationData' % ci_url

# 答题登录
login_h5 = '%s/api/collection/login' % ci_url

# 新增方案专用计算变量
add_solution_group_calculation_url_ci = '%s/api/rule/solutionCalcuVariable' % ci_url

# 新增方案专用显示变量
add_solution_group_display_url_ci = '%s/api/rule/solutionDisplayVariable' % ci_url

# 新增方案项
add_project_item_url_ci = '%s/api/rule/solutionItem' % ci_url

# 新增方案组成
add_solution_composition_url_ci = '%s/api/rule/solutionComposition' % ci_url

# 新增方案评定
add_scheme_evaluation_url_ci = '%s/api/rule/solutionAssessment' % ci_url

def log():
    # 声场logger对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 日志以屏幕形式输出
    console = logging.StreamHandler()
    # console.setLevel(logging.INFO)

    # 把handle对象绑定到logger
    logger.addHandler(console)

    # 生成formatter对象
    console_formatter = logging.Formatter('%(name)s - %(asctime)s - %(module)s - %(levelname)s - %(message)s')

    console.setFormatter(console_formatter)

    return logger


def println(status, value):
    if status == 1:
        print('\033[34m%s is pass' % value)
    elif status == 2:
        print('\033[31m%s is fail' % value)
