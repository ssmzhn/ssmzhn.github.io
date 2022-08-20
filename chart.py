import json
chart_dict = json.load(open('chart.json'))
s = ""
s+="# Phigros v2.3.3 曲目信息\n\n"
s+="数据来源: 萌娘百科\n"
for x in chart_dict:
    s+="### {}\n".format(x)
    s+="\n"
    s+="![]({})\n".format(chart_dict[x]['illustration'])
    s+="- 曲师: {}\n".format(chart_dict[x]['composer'])
    s+="- 所属章节: {}\n".format(chart_dict[x]['chapter'])
    s+="- BPM: {}\n".format(chart_dict[x]['bpm'])
    s+="- 歌曲长度: {}\n".format(chart_dict[x]['length'])
    s+="- 画师: {}\n".format(chart_dict[x]['illustrator'])
    s+="- 谱面信息: \n"
    for y in chart_dict[x]['chart']:
        s+="  - {}\n".format(y)
        s+="    - 定级: {}\n".format(chart_dict[x]['chart'][y]['level'])
        s+="    - 定数: {}\n".format(chart_dict[x]['chart'][y]['difficulty'])
        s+="    - 物量: {}\n".format(chart_dict[x]['chart'][y]['combo'])
        s+="    - 谱师: {}\n".format(chart_dict[x]['chart'][y]['charter'])
    s+="\n"
f = open('chart.md','w')
f.write(s)
f.close()
