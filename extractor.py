import re

def helper(filename):
        server_tss=[]
        seq_ids=[]
        deltas=[]
        with open(filename, "r", encoding="utf-8") as f:
          for line in f:
           # print(line)
            V = re.match(r'.*server_ts:(\d+), seq_id:(\d+), time_delta:(\d+)', line)
            server_ts = V.group(1)
            seq_id = V.group(2)
            delta = V.group(3)
            server_tss.append(server_ts)
            seq_ids.append(seq_id)
            deltas.append(delta)
        # print(server_ts, seq_id, delta)
          print(len(server_tss), len(seq_ids), len(deltas))
          zipped = list(zip(server_tss, seq_ids, deltas))
          #print(list(zipped))
          print(len(zipped))
          validDelta = []
          for x in zipped:
            if x[0] < x[1]:
              continue
            if int(x[2]) > 2000:
              continue
            validDelta.append(int(x[2]))
          print(len(validDelta))
          print(filename, "avg delta", sum(validDelta)/len(validDelta))
def helper1(filename, method):
        server_tss=[]
        seq_ids=[]
        peerids=[]
        with open(filename, "r", encoding="utf-8") as f:
          for line in f:
           # print(line)
            V = re.match(r'.*server_ts=(\d+).*seq_id=(\d+).*method=LiveQueryNodes.*peerid=(\S+)', line)
            if not V:
              continue
            server_ts = V.group(1)
            seq_id = V.group(2)
            peerid= V.group(3)
            server_tss.append(server_ts)
            seq_ids.append(seq_id)
            peerids.append(peerid)
        # print(server_ts, seq_id, delta)
          print(len(server_tss), len(seq_ids), len(peerids))
          zipped = list(zip(server_tss, seq_ids, peerids))
          #print(list(zipped))
          print(len(zipped))
          validDelta = []
          for x in zipped:
            if x[0] < x[1]:
              continue
            delta = int(x[0]) - int(x[1])
            if delta >  2000:
              continue
            validDelta.append(delta)
          print(len(validDelta))
          print(filename, method, "avg delta", sum(validDelta)/len(validDelta))

# helper("keepalive.log")
# helper("querynodes.log")
helper1("access15.log", "LiveQueryNodes")
