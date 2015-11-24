from PyQt4 import QtCore


class TaskChunkStateSnapshot:
    def __init__(self, chunk_id, cpu_power, est_time_left, progress, chunk_short_desc):
        self.chunk_id = chunk_id
        self.cpu_power = cpu_power
        self.est_time_left = est_time_left
        self.progress = progress
        self.chunk_short_desc = chunk_short_desc

    def get_chunk_id(self):
        return self.chunk_id

    def get_cpu_power(self):
        return self.cpu_power

    def get_estimated_time_left(self):
        return self.est_time_left

    def get_progress(self):
        return self.progress

    def get_chunk_short_descr(self):
        return self.chunk_short_desc


class LocalTaskStateSnapshot:
    def __init__(self, task_id, total_tasks, active_tasks, progress, task_short_desc):
        self.task_id = task_id
        self.total_tasks = total_tasks
        self.active_tasks = active_tasks
        self.progress = progress
        self.task_short_desc = task_short_desc

    def get_task_id(self):
        return self.task_id

    def get_total_tasks(self):
        return self.total_tasks

    def get_active_tasks(self):
        return self.active_tasks

    def get_progress(self):
        return self.progress

    def get_task_short_desc(self):
        return self.task_short_desc


# FIXME: REGISTER number of local and remote tasks processed by current node (and number of successes and failures as well) - and show it in this manager
# FIXME: also add a boolean flag indicating whether there is any active local/rempote task being calculated
class NodeStateSnapshot:
    def __init__(self, running=True, uid=0, peers_num=0, tasks_num=0, endpoint_addr="", endpoint_port="",
                 last_network_messages=None, last_task_messages=None, tcss=None, ltss=None):
        if last_network_messages is None:
            last_network_messages = []
        if last_task_messages is None:
            last_task_messages = []
        if tcss is None:
            tcss = {}
        if ltss is None:
            ltss = {}
        self.uid = uid
        self.timestamp = QtCore.QTime.currentTime()
        self.endpoint_addr = endpoint_addr
        self.endpoint_port = endpoint_port
        self.peers_num = peers_num
        self.tasks_num = tasks_num
        self.last_network_messages = last_network_messages
        self.last_task_messages = last_task_messages
        self.task_chunk_state = tcss
        self.local_task_state = ltss
        self.running = running

    def is_running(self):
        return self.running

    def get_uid(self):
        return self.uid

    def get_formatted_timestamp(self):
        return self.timestamp.toString("hh:mm:ss.zzz")

    def get_endpoint_addr(self):
        return self.endpoint_addr

    def get_endpoint_port(self):
        return self.endpoint_port

    def get_peers_num(self):
        return self.peers_num

    def get_tasks_num(self):
        return self.tasks_num

    def get_last_network_messages(self):
        return self.last_network_messages

    def get_last_task_messages(self):
        return self.last_task_messages

    def get_task_chunk_state_snapshot(self):
        return self.task_chunk_state

    def get_local_task_state_snapshot(self):
        return self.local_task_state

    def __str__(self):
        return "Nothing here"
        # ret = str(self.get_uid())+ " ----- \n" + "peers count: " + str(self.get_peers_num()) + "\n" + "tasks count: " + str(self.get_tasks_num()) + "\n"
        # ret += "remote progress: " + str(self.getRemoteProgress()) + "\n" + "lockal progress: " + str(self.getLocalProgress()) + "\n"
        # ret += "last net comunication: " + str(self.get_last_network_messages()) + "\n"
        # ret += "last task comunication: " + str(self.get_last_task_messages())
        # return ret


if __name__ == "__main__":
    ns = NodeStateSnapshot("some uiid", 0.2, 0.7)

    print ns.get_uid()
    print ns.get_formatted_timestamp()
    print ns.getLocalProgress()
    print ns.getRemoteProgress()
