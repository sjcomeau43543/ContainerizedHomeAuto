job "event-handler" {
	datacenters = ["dc1"]
	type = "batch"

    meta {
        id = ""
        status = ""
    }

	parameterized {
        meta_required = ["id","status"]
	}

	group "event-handler-group" {
		count = 1
		task "event-handler-task" {
			driver = "raw_exec"
			config {
				command = "/bin/bash"
				args = [
					"-c",
                    "/home/pirate/event_handler.sh ${NOMAD_META_ID} ${NOMAD_META_STATUS}"
				]
			}
		}
	}
}
