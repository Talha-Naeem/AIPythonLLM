from crewai.flow.flow import Flow,start, listen
from litellm import completion

class CityFun(Flow):
    
    @start()
    def fun2(self):
        result = completion(
            model= "gemini/gemini-1.5-pro",
            api_key = "AIzaSyD43lBBFVc7wzfg2dYV1trByz20mtXZmFo",
            messages=[{"content":"How tell to the introvert girl that I love you.",
            "role":"user"}]
        )
        con = result['choices'][0]['message']['content'].strip()
        print(con)
        return con

    @listen(fun2)
    def fun3(self,con):
        result = completion(
            model= "gemini/gemini-1.5-pro",
            api_key = "AIzaSyD43lBBFVc7wzfg2dYV1trByz20mtXZmFo",
            messages=[{"content":"fBased on the topic '{con}', tell how can i find a place where i talk to her, either we are working in a same office but in different team and floor.",
            "role":"user"}]
        )
        outline = result['choices'][0]['message']['content'].strip()
        print(outline)
        return outline
        self.state = ["fun_fact"]
    
    @listen(fun3)
    def fun4(self,con):
        with open("funfact.md","w") as f:
            f.write(self.state["fun_fact"])
            return self.state["fun_fact"]

def kickoff():
    fa = CityFun()
    fa.kickoff()