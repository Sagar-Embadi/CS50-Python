def main():
    emo=input()
    result = convert(emo)
    print(result)
def convert(emo):
    emo1=emo.replace(":)","🙂")
    emo2=emo1.replace(":(","🙁")
    return emo2
main()
