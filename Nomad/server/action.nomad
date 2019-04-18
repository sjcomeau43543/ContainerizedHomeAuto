job "action" {
	datacenters = ["dc1"]
	type = "batch"

    meta {
        mac = ""
        port = ""
        msg = ""
    }

	parameterized {
        meta_required = ["mac","port","msg"]
	}

	group "action-group" {
		count = 1
		task "action-task" {
			driver = "raw_exec"
			config {
				command = "/bin/bash"
				args = [
					"-c",
                    "echo python2 automate.py write ${NOMAD_META_MAC} ${NOMAD_META_PORT} ${NOMAD_META_MSG} | sudo tee -a /home/pirate/test.txt"
				]
			}
		}
	}
}
