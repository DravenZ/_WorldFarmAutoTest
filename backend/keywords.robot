# Created by Heng Xin
# Date: 2018-08-20

*** Settings ***
Resource    variables.robot
Library     Main.py

*** Keywords ***
中介发布农场
    Log    ${手机号}
    Log    ${密码}
    Log    ${农场名}
    Log    ${农场类型}
    Log    ${价格范围}
    Log    ${面积范围}
    seller agent add farm    ${手机号}    ${密码}    ${农场名}    ${农场类型}    ${州名}    ${价格范围}    ${面积范围}
买家查询农场
    Log    ${农场类型}
    Log    ${价格范围}
    Log    ${面积范围}
