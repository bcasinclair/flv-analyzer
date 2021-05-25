import json

# flv_analyzer output for a video frame
# e.g. ./analyze sample.flv > output.json
ff= {
      "Prev tag size": 346,
      "Tag type": "9 - Video data",
      "Data size": 8304,
      "Timestamp": 1619,
      "Timestamp extended": 0,
      "StreamID": 0,
      "VideoData": {
        "Frame type": "2 - inter frame (for AVC, a non-seekable frame)",
        "Codec ID": "7 - AVC"
      },
      "AVC video tag": {
        "AVC packet type": "1 - AVC NALU",
        "AVC composition time": 0
      }
    },

f = open("output.json")

fjs = json.loads(f.read())

last_pts = 0
last_I = 0
count = 0
print("framecount, timestamp, timestamp_diff, frame_type")
for frame in fjs["frames"]:
    if "Tag type" in frame and frame["Tag type"] == "9 - Video data":
        if frame["VideoData"]["Frame type"] == "1 - keyframe (for AVC, a seekable frame)":
            frame_type = "I"
            print("%d, %d, %d, I" % (count, frame["Timestamp"], frame["Timestamp"] - last_pts))
            last_pts = frame["Timestamp"]
        count +=1

