import pyttsx3
import time
names=["wang","li","zhao"]
colors=["red","green","blue"]
dict={name:color for name in names for color in colors}
print(dict)
start=time.time()
engine = pyttsx3.init()
#engine.say("君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不愿醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。")
engine.say("青青子衿，悠悠我心，但为君故，沉吟至今")
engine.runAndWait()
print(time.time()-start)
#python -m cProfile -o c:/pythonproject/day01/output.prof -s tottime c:/pythonproject/day01/test3.py