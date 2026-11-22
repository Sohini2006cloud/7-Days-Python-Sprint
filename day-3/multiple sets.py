riya_done={"t1", "t2", "t3", "t5"}
kabir_done={"t2", "t3", "t5"}
ananya_done={"t3","t4", "t5"}

finished_task= riya_done & kabir_done & ananya_done
print("Tasks that are done by all three of them are: ",finished_task)
kabir_ananya= kabir_done | ananya_done
task_riya= riya_done - kabir_ananya
print("Tasks that are only done by Riya: ",task_riya)
all_task= riya_done | kabir_ananya
print("tasks that are done by atleast one are: ",all_task) 