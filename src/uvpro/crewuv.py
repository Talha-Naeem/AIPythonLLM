from crewai.flow.flow import Flow,start, listen

class SimpleFlow(Flow):
    
    @listen(fun3)
    def fun1(self):
        print("fa 1")
    
    @start()
    def fun2(self):
        print("fa 2")

    @listen(fun2)
    def fun3(self):
        print("fa 3")

def kickoff():
    fa = SimpleFlow()
    fa.kickoff()