from PIL import Image,ImageDraw,ImageFont,ImageSequence
import matplotlib.pyplot as plt
import json
import turtle as t
import webbrowser, os
from pyecharts import Bar,Line,Pie
def bqbzz(openimg,size=30,rotate=0,color=(0,0,0),ttf=None,text="我\n真\n是\n个\n大\n聪\n明"):
    img = Image.open(openimg)
    nimg = Image.new("RGBA",(1000,1000))
    draw = ImageDraw.Draw(nimg)
    if ttf is not None:
        font = ImageFont.truetype(ttf,size)
    draw.text((10, 10), text, font=font, fill=color)
    nimg = nimg.rotate(rotate, expand=True)
    img.paste(nimg,(0,0),nimg)
    plt.imshow(img)
    plt.show()
def json_rw(filename,mode):
    with open(filename, mode) as f:
        conect = json.load(f)
    return conect
def finder(lst):
    for i in range(len(lst)):
        n += 1
        if wtg == lst[i]:
            return str("查询了",n,"次找到了","是第",i+1,"个")
    else:
        return "没找到"
def IDNumber_Tool(idnum):
    lone = len(idnum)
    while len(idnum) != 18:
        return "位数不对"
        #1234567891  2  3  4  5  6   7   8   9  1
        #0123456789[10][11][12][13][14][15][16][17]
    else:
        if int(idnum[16]) % 2 == 0:
            xb = "女"
        else:
            xb = "男"
        year = int(idnum[6:10])
        month = int(idnum[10:12])
        day = int(idnum[12:14])
        return str(xb,"year:",year,"month:",month,"day:",day)
def tgt(x=0,y=0):
    t.up()
    t.goto(x,y)
    t.pd()
def hundred_people_name():
    t.speed(0)
    t.ht()
    lista = ['李', '王', '张', '刘', '陈', '杨', '赵', '黄', '周', '吴', '徐', '孙', '胡',
 '朱', '高', '林', '何', '郭', '马', '罗', '梁', '宋', '郑', '谢', '韩', '唐', '冯', '于'
, '董', '萧', '程', '曹', '袁', '邓', '许', '傅', '沈', '曾', '彭', '吕','苏', '卢', '蒋', '蔡', 
'贾', '丁', '魏', '薛', '叶', '阎', '余', '潘', '杜', '戴', '夏', '钟', '汪', '田', '任', '姜', '范', '方',
 '石', '姚', '谭', '廖', '邹', '熊', '金', '陆','郝', '孔', '白', '崔', '康', '毛', '邱', '秦', '江', '史', '顾', 
 '侯', '邵', '孟', '龙', '万', '段', '漕', '钱', '汤', '尹', '黎', '易', '常', '武', '乔', '贺', '赖', '龚', '文']
    def draw(info):
        index = 0
        for k in range(10):
            for j in range(10):
                x = -250 + j * 50
                y = 250 - 50*k
                tgt(x, y)
                for i in range(4):
                    t.fd(50)
                    t.rt(90)
                tgt(x + 25, -25-15+y)
                t.write(lista[index], align="center", font=("华文新魏", 20, "normal"))
                index += 1
        tgt(0,-300)
        t.write(info, align="center", font=("华文新魏", 25, "normal"))
    draw()
def summon_gif(gif_dir,sort_reverse=False,ext_file=[".png",".jpg",".jpeg",".bmp"],output_name="Deflut.gif",txt="",ttf="STXINGKA.TTF",textxy=(80,600),size=80,ttf_color=(0,0,0),use_own_color_list=False,own_color_list=[(0,0,0)]):
    fir = gif_dir
    files = sorted(os.listdir(fir), reverse=sort_reverse)
    frames = []
    font = ImageFont.truetype(ttf,size)
    if use_own_color_list == False:
        for file in files:
            name, ext = os.path.splitext(file)
            if ext in ext_list:
                img = Image.open("{}{}{}".format(fir, os.sep, file))
                draw = ImageDraw.Draw(img)
                draw.text(textxy,txt,ttf_color,font=font)
                frames.append(img)
    else:
        index = len(own_color_list)
        for i in range(len(files)):
            name, ext = os.path.splitext(file)
            if ext in ext_list:
                img = Image.open("{}{}{}".format(fir, os.sep, file))
                draw = ImageDraw.Draw(img)
                draw.text(textxy,txt,own_color_list[index%i],font=font)
                frames.append(img)
    frames[0].save(output_name, append_images=frames[1:], save_all=True)
    webbrowser.open("file://"+os.path.realpath(output_name))
def draw_table(tpe,attr,value,value2=None,attr2=None):
    if tpe == "Bar":
        chart = Bar("Deflut_Bar")
    elif tpe == "Line":
        chart = Line("Deflut_Line")
    else:
        chart = Pie("Deflut_Pie")
    chart.add(tpe,attr,value)
    chart.render()
    webbrowser.open("file://"+os.path.realpath("render.html"))