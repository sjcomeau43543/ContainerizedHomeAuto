job "test" {
	datacenters = ["dc1"]
	type = "batch"
	parameterized {
	}

	group "test-group" {
		count = 1
		task "test-task" {
			driver = "raw_exec"
			config {
				command = "/bin/bash"
				args = [
					"-c",
					"echo hello | sudo tee -a /home/pirate/test.txt "
				]
			}
		}
	}
}
