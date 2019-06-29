import tkinter as tk
import topActor
import topCount
import topScore
import topYear
import tuopu
class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="猫眼电影前100部数据分析:")
        self.submit1 = tk.Button(self, text="演员电影作品数量排名", command = topActor.topActorOutnput,width=40)
        self.submit2= tk.Button(self, text="各国/地区电影数量排名", command=topCount.topCountOuput, width=40)
        self.submit3 = tk.Button(self, text="电影评分最高top10", command=topScore.topScoreOutput, width=40)
        self.submit4 = tk.Button(self, text="电影数量年份排名", command = topYear.topYearOuput,width=40)
        self.submit5 = tk.Button(self, text="前30部电影与演员之间的关系", command=tuopu.tuopuOutput, width=40)

        self.prompt.pack(side="top")

        # lay the widgets out on the screen.
        self.submit1.pack(side="top")
        self.submit2.pack(side="top")
        self.submit3.pack(side="top")
        self.submit4.pack(side="top")
        self.submit5.pack(side="top")


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()