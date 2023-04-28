#python3

class Gyoretsu():
    def __init__(self):
        pass

    def inputf(self, x):
        while True:
            print()
            print(f"行列{x}を入力してください。")
            print("------------------------------------")
            print("各要素間 : 1マスのスペース")
            print("  改行   : / を入力")
            print("------------------------------------")
            out = [i.split() for i in input(" >> ").split("/")]; tf = False
            for i in range(len(out)):
                for k in range(len(out[i])):
                    try: out[i][k] = int(out[i][k])
                    except: tf = True; break
                if tf: break
            if tf: print("ERR 数字と / 以外は使用できません。")
            else: return out

    def tenchif(self, x):
        out = [[None for i in range(len(x))] for i in range(len(x[0]))]
        for i in range(len(x)):
            for k in range(len(x[i])):
                out[k][i] = x[i][k]
        return out

    def waf(self, x, y):
        if len(x) != len(y):
            print("ERR 行数が異なるので、和は定義されません。")
            return
        for i in range(len(x)):
            if len(x[i]) != len(y[i]):
                print("ERR 列数が異なるので、和は定義されません。")
                return
        for i in range(len(x)):
            for k in range(len(x[i])):
                x[i][k] += y[i][k]
        return x
        
    def sekif(self, x, y):
        if len(x[0]) != len(y):
            print("ERR 積は定義されません。")
            return
        out = [[] for _ in range(len(x))]
        for i in range(len(x)):
            for k in range(len(y[0])):
                temp = 0
                for s in range(len(y)):
                    temp += y[s][k]*x[i][s]
                out[i].append(temp)
        return out

    def input_opef(self):
        while True:
            print()
            print("演算を入力してください。")
            print("------------------------------------")
            print(" 和 : wa")
            print(" 積 : seki")
            print("------------------------------------")
            x = input()
            if x == "wa" or x == "seki":
                return x
            else:
                print("ERR 既定の演算を入力してください。")


if __name__ == "__main__":
    g = Gyoretsu()
    #input
    prev = g.inputf("prev")
    aftr = g.inputf("aftr")
    ope = g.input_opef(); print()
    #calc
    ans = g.waf(prev, aftr) if ope == "wa" else g.sekif(prev, aftr) if ope == "seki" else "ERR 定義されていない演算子です。"
    #output
    if ans != None:
        print("--- answer ---")
        for i in ans:
            print(i)
