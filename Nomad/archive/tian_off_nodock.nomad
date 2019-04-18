job "tian_off_nodock" {
	datacenters = ["dc1"]
	type = "batch"

	group "group1" {
		count = 1
		task "tian_off_nodock_task" {
			driver = "raw_exec"
			config {
				command = "/bin/bash"
				args = ["-c", 
				"sudo python /home/pirate/automate.py -w -b -m 98:D3:A1:FD:49:8D -t 0"]
			}
		}
	}
}
