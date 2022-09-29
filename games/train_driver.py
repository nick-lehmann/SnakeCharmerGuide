"""
🚂 Train Driver
You are driving a train from Berlin to Paris.
On the way to Paris you will stop in Hamburg, Amsterdam and Brussels before arriving in Paris.
Every time you depart you will need to tell the passengers that you are departing and what the next stop will be.
In Paris tell the passengers that that is the last stop.

Bonus Points: Do all the prints inside the loop.
"""

stops = ["Berlin", "Hamburg", "Amsterdam", "Brussels", "Paris"]
total_stops = len(stops)

for i in range(total_stops):
    if total_stops - 1 > i:
        print(f"🚂 Departing from {stops[i]}")
        print(f"⏰ Next stop {stops[i+1]}")
    else:
        print(f"👋 {stops[i]} is the last stop")
    print()
