# 图片绘制

from typing import List
import turtle as te

# 调用了自己写的专门处理图片信息的函数, 将图片每2x2个px的颜色取平均值，返回由R, G, B三个通道的矩阵以及图片的高与宽构成的列表
from picProcessor import processor


# 图片路径参数
path = ".\\pic.png"
    
# 逐列绘制图像
def drawLine(t: te.Turtle, imginfo: List = None):
    '''
    让turtle跑起来的函数逐列打印图像
    
    Args:
        t: turtle库的Turtle对象
        imginfo: 由picprocessor.processor()返回的图像信息, 包含图像的hex信息以及图片的高和宽
    '''
    
    # 将imginfo拆解
    imgcolor = imginfo[0]
    height = imginfo[1]
    width = imginfo[2]

    # 初始化画笔，移动至起始位置(图片左上角)
    t.up()
    t.goto(-width/2,height/2)
    
    # 逐列打印图像, 根据所给的画笔序号和数量分配该画笔需要打印的列
    for col in range(0, int(width/2)):
        for row in range(int(height/2)):
            posx = -width/2 + col*2
            posy = height/2 - row*2
            
            color = imgcolor[row][col]
            
            # 移动画笔，落笔
            t.pencolor(color)
            t.pensize(2)
            t.goto(posx,posy)
            t.down()
            t.goto(posx,posy)
            
        # 每画完一列，提起画笔，防止不同列因画笔移动而污染
        t.up()
        te.Screen().update()
        
        

def main():
    
    # 根据图片路径处理图片，返回图片信息
    imginfo = processor(path)
    height = imginfo[1]
    width = imginfo[2]
    
    # 创建一个比原图稍大的黑底画布
    screen = te.Screen()
    screen.setup(width+50, height+50)
    screen.bgcolor("black")
    # 若使用RGB定义画笔颜色，需要启用下列代码
    # screen.colormode(255)
    
    t = te.Turtle()
    screen.tracer(False)
    drawLine(t,imginfo)
    te.done()

if __name__ == "__main__":
    main()
