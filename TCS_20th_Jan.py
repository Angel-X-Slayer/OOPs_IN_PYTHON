class scholar:
    def __init__(self, scid,name, marks, state):
        self.scid=scid
        self.name=name
        self.marks=marks
        self.state=state
class scholargrade:
    def __init__(self):
        self.scgrad=[]
        self.scgrad1=[]
    def calculate_grade(self,list,grade):
        key_list=["scid","name","state","grade","total_marks"]
        assign_grade=""
        if len(list)==0:
            return None
        else:
            for i in list:
                dict1={}
                total_marks=sum(i.marks)
                percentage=int(total_marks/3)
                if percentage>80:
                    assign_grade="A"
                elif percentage<80 and total_marks>70:
                    assign_grade="B"
                elif percentage<70 and total_marks>60:
                    assign_grade="C"
                else:
                    assign_grade="D"
                student_list=[i.scid,i.name,i.state,assign_grade,total_marks]
                dict2=dict(zip(key_list,student_list))
                self.scgrad1.append(dict2)
                if student_list[3]==grade:

                    dict1=dict(zip(key_list,student_list))
                    self.scgrad.append(dict1)
                
        print(self.scgrad1)  ## Data of all students

        self.scgrad=sorted(self.scgrad,key=lambda x: (x['total_marks']), reverse=False)  ## Data of students who got grade A
        return(self.scgrad)

    def paas_fail_ratio(self):
        pass_fail_ratio=[]
        state=[]
        for i in self.scgrad1:
            # print(i)
            state.append(i["state"])
        states = list(set([l["state"] for l in self.scgrad1]))
        # print(state)
        for i in states:
            totstu=0
            totfail=0

            for j in self.scgrad1:
                if i==j["state"]:
                    totstu+=1
                    if j["grade"]!="A":
                        totfail+=1 
            fail_percentage = int(round((totfail/totstu) * 100, 0))
            totpass=totstu-totfail
            pass_percentage = int(round((totpass /totstu) * 100, 0))
            one_state_record = [i, f'{pass_percentage}:{fail_percentage}']
            pass_fail_ratio.append(one_state_record)
        return(pass_fail_ratio)




        






if __name__=="__main__":
    k=int(input())
    obj_list=[]
    for i in range(k):
        scid=int(input())
        name=input().lower()
        state=input().lower()
        mark1=int(input())
        mark2=int(input())
        mark3=int(input())
        marks=[mark1,mark2,mark3]
        sc_obj_1=scholar(scid,name,marks,state)
        obj_list.append(sc_obj_1)
    
    # print("the output is :")

    # for i in obj_list:
    #     print(i.scid)
    #     print(i.name)
    #     print(i.state)
    #     print(i.marks)
    #     print()
    

    grade=input().upper()
    sc_obj_2=scholargrade()
    calculation=sc_obj_2.calculate_grade(obj_list,grade)
    for i in calculation:
        print(i)  
    calculation2=sc_obj_2.paas_fail_ratio()
    for i in calculation2:
        print(i)
