#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_CENTER
import copy

style = getSampleStyleSheet()
whiteParaStyle = ParagraphStyle('whiteParaStyle',parent=style['BodyText'],textColor="white",alignment=TA_CENTER)
greyParaStyle = ParagraphStyle('greyParaStyle',parent=style['BodyText'],textColor="#443e42")
#Read a CSV to make this data?
dataDictionary = {"Mozambique":{}}
dataDictionary["Mozambique"]["country"] = "Mozambique"
dataDictionary["Mozambique"]["table1"] = [["Gini index score*",Paragraph("Gini index rank<super>†</super>",style=whiteParaStyle),"Year"],[51,125,2011]]
dataDictionary["Mozambique"]["table2"] = [
    ["Population (000)",format(12428,",d"),2015]
    ,["Under-5 population (000)",format(1935,",d"),2015]
    ,["Urban (%)",format(20,",d"),2015]
    ,[">65 years (%)",format(5,",d"),2015]
    ]
dataDictionary["Mozambique"]["table3"] = [
    ["Number of children under 5 affected (000)","",""]
    ,[Paragraph("Stunting<super>a</super>",style=greyParaStyle),format(733,",d"),2015]
    ,[Paragraph("Wasting<super>a</super>",style=greyParaStyle),format(43,",d"),2015]
    ,[Paragraph("Overweight<super>a</super>",style=greyParaStyle),format(149,",d"),2015]
    ,["Percentage of children under 5 affected","",""]
    ,[Paragraph("Wasting<super>a</super>",style=greyParaStyle),format(2,"d"),2015]
    ,[Paragraph("Severe wasting<super>a</super>",style=greyParaStyle),format(1,"d"),2015]
    ,[Paragraph("Overweight<super>a</super>",style=greyParaStyle),format(8,"d"),2015]
    ,[Paragraph("Low birth weight<super>b</super>",style=greyParaStyle),format(7,"d"),2015]
    ]
dataDictionary["Mozambique"]["table4"] = [
    [Paragraph("Adolescent overweight<super>a</super>",style=greyParaStyle),"NA","NA"]
    ,[Paragraph("Adolescent obesity<super>a</super>",style=greyParaStyle),"NA","NA"]
    ,[Paragraph("Women of reproductive age, thinness<super>b</super>",style=greyParaStyle),format(5,"d"),2010]
    ,[Paragraph("Women of reproductive age, short stature<super>b</super>",style=greyParaStyle),format(2,"d"),2010]
]
dataDictionary["Mozambique"]["table5"] = [
    [Paragraph("Women of reproductive age with anemia<super>a</super>",style=greyParaStyle),"",""]
    ,["Total population affected (000)",format(467,",d"),2011]
    ,["Total population affected (%)",format(17,"d"),2011]
    ,[Paragraph("Vitamin A deficiency in children 6-59 months old (%)<super>b</super>",style=greyParaStyle),format(39,"d"),2013]
    ,[Paragraph("Population classification of iodone nutrition (age group 5-19)<super>c</super>",style=greyParaStyle),Paragraph("Risk of iodine-induced hyperthyroidism (IIH) within 5-10 years following introduction of iodized salt in susceptible groups)",style=greyParaStyle),1996]
]
dataDictionary["Mozambique"]["table6"] = [
    [
        Paragraph("<b>Under-5 stunting, 2015<super>a</super></b>",style=whiteParaStyle)
        ,Paragraph("<b>Under-5 wasting, 2015<super>b</super></b>",style=whiteParaStyle)
        ,Paragraph("<b>Under-5 overweight, 2015<super>a</super></b>",style=whiteParaStyle)
        ,Paragraph("<b>WRA Anemia, 2011<super>b</super></b>",style=whiteParaStyle)
        ,Paragraph("<b>EBF, 2014-2015<super>a</super></b>",style=whiteParaStyle)
     ]
    ,["Off course, some progress","On course","Off course, no progress","Off course","On course"]
]

dataDictionary["Afghanistan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Albania"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Algeria"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Andorra"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Angola"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Antigua and Barbuda"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Argentina"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Armenia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Australia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Austria"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Azerbaijan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Bahamas"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Bahrain"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Bangladesh"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Barbados"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Belarus"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Belgium"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Belize"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Benin"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Bhutan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Bolivia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Bosnia and Herzegovina"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Botswana"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Brazil"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Brunei Darussalam"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Bulgaria"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Burkina Faso"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Burundi"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Cambodia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Cameroon"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Canada"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Cape Verde"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Central African Republic"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Chad"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Chile"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["China"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Colombia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Comoros"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Congo (Republic of the)"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Costa Rica"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Cote d'Ivoire"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Croatia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Cuba"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Cyprus"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Czech Republic"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Democratic People's Republic of Korea"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Democratic Republic of the Congo"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Denmark"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Djibouti"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Dominica"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Dominican Republic"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Ecuador"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Egypt"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["El Salvador"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Equatorial Guinea"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Eritrea"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Estonia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Ethiopia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Fiji"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Finland"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["France"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Gabon"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Gambia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Georgia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Germany"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Ghana"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Greece"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Grenada"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Guatemala"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Guinea"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Guinea-Bissau"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Guyana"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Haiti"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Honduras"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Hungary"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Iceland"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["India"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Indonesia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Iran"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Iraq"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Ireland"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Israel"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Italy"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Jamaica"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Japan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Jordan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Kazakhstan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Kenya"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Kiribati"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Kuwait"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Kyrgyzstan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Lao People's Democratic Republic"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Latvia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Lebanon"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Lesotho"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Liberia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Libya"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Liechtenstein"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Lithuania"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Luxembourg"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Madagascar"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Malawi"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Malaysia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Maldives"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Mali"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Malta"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Marshall Islands"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Mauritania"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Mauritius"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Mexico"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Micronesia (Federated States of)"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Monaco"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Mongolia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Montenegro"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Morocco"] = copy.deepcopy(dataDictionary["Mozambique"])
# dataDictionary["Mozambique"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Myanmar"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Namibia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Nauru"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Nepal"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Netherlands"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["New Zealand"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Nicaragua"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Niger"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Nigeria"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Norway"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Oman"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Pakistan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Palau"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Panama"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Papua New Guinea"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Paraguay"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Peru"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Philippines"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Poland"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Portugal"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Qatar"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Republic of Korea"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Republic of Moldova"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Romania"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Russian Federation"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Rwanda"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Saint Kitts and Nevis"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Saint Lucia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Saint Vincent and the Grenadines"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Samoa"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["San Marino"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Sao Tome and Principe"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Saudi Arabia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Senegal"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Serbia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Seychelles"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Sierra Leone"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Singapore"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Slovakia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Slovenia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Solomon Islands"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Somalia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["South Africa"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["South Sudan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Spain"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Sri Lanka"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Sudan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Suriname"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Swaziland"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Sweden"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Switzerland"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Syria"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Tajikistan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Thailand"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["The former Yugoslav Republic of Macedonia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Timor-Leste"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Togo"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Tonga"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Trinidad and Tobago"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Tunisia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Turkey"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Turkmenistan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Tuvalu"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Uganda"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Ukraine"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["United Arab Emirates"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["United Kingdom"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["United Republic of Tanzania"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["United States of America"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Uruguay"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Uzbekistan"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Vanuatu"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Venezuela"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Viet Nam"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Yemen"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Zambia"] = copy.deepcopy(dataDictionary["Mozambique"])
dataDictionary["Zimbabwe"] = copy.deepcopy(dataDictionary["Mozambique"])

for country in dataDictionary.keys():
    dataDictionary[country]["country"] = country
    
    # dataDictionary["Mozambique"]["table1"] = [["Gini index score*",Paragraph("Gini index rank<super>†</super>",style=whiteParaStyle),"Year"],[51,125,2011]]
    dataDictionary[country]["table1"][1] = [51,125,2011]
    
    # dataDictionary["Mozambique"]["table2"] = [
    #     ["Population (000)",format(12428,",d"),2015]
    #     ,["Under-5 population (000)",format(1935,",d"),2015]
    #     ,["Urban (%)",format(20,",d"),2015]
    #     ,[">65 years (%)",format(5,",d"),2015]
    #     ]
    dataDictionary[country]["table2"][0][1] = format(12428,",d")
    dataDictionary[country]["table2"][0][2] = 2015
    dataDictionary[country]["table2"][1][1] = format(1935,",d")
    dataDictionary[country]["table2"][1][2] = 2015
    dataDictionary[country]["table2"][2][1] = format(20,",d")
    dataDictionary[country]["table2"][2][2] = 2015
    dataDictionary[country]["table2"][3][1] = format(5,",d")
    dataDictionary[country]["table2"][3][2] = 2015
    # dataDictionary["Mozambique"]["table3"] = [
    #     ["Number of children under 5 affected (000)","",""]
    #     ,[Paragraph("Stunting<super>a</super>",style=greyParaStyle),format(733,",d"),2015]
    #     ,[Paragraph("Wasting<super>a</super>",style=greyParaStyle),format(43,",d"),2015]
    #     ,[Paragraph("Overweight<super>a</super>",style=greyParaStyle),format(149,",d"),2015]
    #     ,["Percentage of children under 5 affected","",""]
    #     ,[Paragraph("Wasting<super>a</super>",style=greyParaStyle),format(2,"d"),2015]
    #     ,[Paragraph("Severe wasting<super>a</super>",style=greyParaStyle),format(1,"d"),2015]
    #     ,[Paragraph("Overweight<super>a</super>",style=greyParaStyle),format(8,"d"),2015]
    #     ,[Paragraph("Low birth weight<super>b</super>",style=greyParaStyle),format(7,"d"),2015]
    #     ]
    dataDictionary[country]["table3"][1][1] = format(733,",d")
    dataDictionary[country]["table3"][1][2] = 2015
    dataDictionary[country]["table3"][2][1] = format(43,",d")
    dataDictionary[country]["table3"][2][2] = 2015
    dataDictionary[country]["table3"][3][1] = format(149,",d")
    dataDictionary[country]["table3"][3][2] = 2015
    dataDictionary[country]["table3"][5][1] = format(2,",d")
    dataDictionary[country]["table3"][5][2] = 2015
    dataDictionary[country]["table3"][6][1] = format(1,",d")
    dataDictionary[country]["table3"][6][2] = 2015
    dataDictionary[country]["table3"][7][1] = format(8,",d")
    dataDictionary[country]["table3"][7][2] = 2015
    dataDictionary[country]["table3"][8][1] = format(7,",d")
    dataDictionary[country]["table3"][8][2] = 2015
    # dataDictionary["Mozambique"]["table4"] = [
    #     [Paragraph("Adolescent overweight<super>a</super>",style=greyParaStyle),"NA","NA"]
    #     ,[Paragraph("Adolescent obesity<super>a</super>",style=greyParaStyle),"NA","NA"]
    #     ,[Paragraph("Women of reproductive age, thinness<super>b</super>",style=greyParaStyle),format(5,"d"),2010]
    #     ,[Paragraph("Women of reproductive age, short stature<super>b</super>",style=greyParaStyle),format(2,"d"),2010]
    # ]
    dataDictionary[country]["table4"][0][1] = "NA"
    dataDictionary[country]["table4"][0][2] = "NA"
    dataDictionary[country]["table4"][1][1] = "NA"
    dataDictionary[country]["table4"][1][2] = "NA"
    dataDictionary[country]["table4"][2][1] = format(5,",d")
    dataDictionary[country]["table4"][2][2] = 2010
    dataDictionary[country]["table4"][3][1] = format(2,",d")
    dataDictionary[country]["table4"][3][2] = 2010
    # dataDictionary["Mozambique"]["table5"] = [
    #     [Paragraph("Women of reproductive age with anemia<super>a</super>",style=greyParaStyle),"",""]
    #     ,["Total population affected (000)",format(467,",d"),2011]
    #     ,["Total population affected (%)",format(17,"d"),2011]
    #     ,[Paragraph("Vitamin A deficiency in children 6-59 months old (%)<super>b</super>",style=greyParaStyle),format(39,"d"),2013]
    #     ,[Paragraph("Population classification of iodone nutrition (age group 5-19)<super>c</super>",style=greyParaStyle),Paragraph("Risk of iodine-induced hyperthyroidism (IIH) within 5-10 years following introduction of iodized salt in susceptible groups)",style=greyParaStyle),1996]
    # ]
    dataDictionary[country]["table5"][1][1] = format(467,",d")
    dataDictionary[country]["table5"][1][2] = 2011
    dataDictionary[country]["table5"][2][1] = format(17,",d")
    dataDictionary[country]["table5"][2][2] = 2011
    dataDictionary[country]["table5"][3][1] = format(39,",d")
    dataDictionary[country]["table5"][3][2] = 2013
    dataDictionary[country]["table5"][4][1] = Paragraph("Risk of iodine-induced hyperthyroidism (IIH) within 5-10 years following introduction of iodized salt in susceptible groups)",style=greyParaStyle)
    dataDictionary[country]["table5"][4][2] = 1996
    # dataDictionary["Mozambique"]["table6"] = [
    #     [
    #         Paragraph("<b>Under-5 stunting, 2015<super>a</super></b>",style=whiteParaStyle)
    #         ,Paragraph("<b>Under-5 wasting, 2015<super>b</super></b>",style=whiteParaStyle)
    #         ,Paragraph("<b>Under-5 overweight, 2015<super>a</super></b>",style=whiteParaStyle)
    #         ,Paragraph("<b>WRA Anemia, 2011<super>b</super></b>",style=whiteParaStyle)
    #         ,Paragraph("<b>EBF, 2014-2015<super>a</super></b>",style=whiteParaStyle)
    #      ]
    #     ,["Off course, some progress","On course","Off course, no progress","Off course","On course"]
    # ]
    dataDictionary[country]["table6"][1] = ["Off course, some progress","On course","Off course, no progress","Off course","On course"]

tableStyles = {}
tableStyles["table1"] = [
    ('TEXTCOLOR',(0,0),(-1,-1),"white")
    ,('BACKGROUND',(0,0),(2,0),"#7b1059")
    ,('FONTNAME',(0,1),(2,1),"Arial-Bold")
    # ,('FONTNAME',(0,1),(2,1),"Arial")
    ,('BACKGROUND',(0,1),(2,1),"#c79ec5")
    # ,('GRID',(0,0),(-1,-1),1,"white")
    ,('LINEAFTER',(0,0),(1,1),1,"white")
    ,('ALIGN',(0,0),(-1,-1),"CENTER")
    ,('VALIGN',(0,0),(-1,-1),"MIDDLE")
    ]
tableStyles["table2"] = [
    ('BACKGROUND',(0,1),(-1,1),"#fef5e7")
    ,('BACKGROUND',(0,3),(-1,3),"#fef5e7")
    ,('ALIGN',(0,0),(0,-1),"LEFT")
    ,('ALIGN',(1,0),(2,-1),"CENTER")
    ,('VALIGN',(0,0),(-1,-1),"MIDDLE")
    ,('BOX',(1,0),(1,-1),1,"#f79c2a")
    ,('LINEABOVE',(0,0),(-1,0),1,"#f79c2a")
    ,('LINEBELOW',(0,-1),(-1,-1),1,"#f79c2a")
    ,('TEXTCOLOR',(0,0),(-1,-1),"#443e42")
    ]
tableStyles["table3"] = [
    ('BACKGROUND',(0,1),(-1,1),"#fef5e7")
    ,('BACKGROUND',(0,3),(-1,3),"#fef5e7")
    ,('BACKGROUND',(0,5),(-1,5),"#fef5e7")
    ,('BACKGROUND',(0,7),(-1,7),"#fef5e7")
    ,('ALIGN',(0,0),(0,-1),"LEFT")
    ,('ALIGN',(1,0),(2,-1),"CENTER")
    ,('VALIGN',(0,0),(-1,-1),"MIDDLE")
    ,('BOX',(1,1),(1,3),1,"#f79c2a")
    ,('BOX',(1,5),(1,-1),1,"#f79c2a")
    ,('LINEABOVE',(0,0),(-1,0),1,"#f79c2a")
    ,('LINEABOVE',(0,1),(-1,1),1,"#f79c2a")
    ,('LINEABOVE',(0,4),(-1,4),1,"#f79c2a")
    ,('LINEABOVE',(0,5),(-1,5),1,"#f79c2a")
    ,('LINEBELOW',(0,-1),(-1,-1),1,"#f79c2a")
    ,('SPAN',(0,0),(-1,0))
    # ,('FONTNAME',(0,0),(-1,0),"Arial-Bold")
    ,('SPAN',(0,4),(-1,4))
    # ,('FONTNAME',(0,4),(-1,4),"Arial-Bold")
    ,('TEXTCOLOR',(0,0),(-1,-1),"#443e42")
    ]
tableStyles["table4"] = tableStyles["table2"]
tableStyles["table5"] = [
    ('LINEABOVE',(0,0),(-1,0),1,"#f79c2a")
    ,('LINEABOVE',(0,1),(-1,1),1,"#f79c2a")
    ,('LINEABOVE',(0,3),(-1,3),1,"#f79c2a")
    ,('LINEBELOW',(0,4),(-1,4),1,"#f79c2a")
    ,('SPAN',(0,0),(-1,0))
    ,('LINEAFTER',(0,1),(1,2),.5,"#fbcd99")
    ,('LINEBELOW',(0,1),(-1,1),.5,"#fbcd99")
    ,('LINEAFTER',(0,3),(1,-1),1,"#fbcd99")
    ,('LINEABOVE',(0,-1),(-1,-1),1,"#fbcd99")
    ,('VALIGN',(0,0),(-1,-1),"MIDDLE")
    ,('ALIGN',(0,0),(0,-1),"LEFT")
    ,('ALIGN',(1,0),(2,-1),"CENTER")
    ,('TEXTCOLOR',(0,0),(-1,-1),"#443e42")
]
tableStyles["table6"] = [
    ('TEXTCOLOR',(0,0),(-1,0),"white")
    # ,('BACKGROUND',(0,0),(-1,0),"#204d5e")
    # ,('BACKGROUND',(0,1),(-1,1),"white")
    # ,('GRID',(0,0),(-1,-1),1,"#386170")
    ,('ALIGN',(0,0),(-1,-1),"CENTER")
    ,('VALIGN',(0,0),(-1,-1),"MIDDLE")
    ,('TEXTCOLOR',(0,1),(-1,-1),"#443e42")
    ]