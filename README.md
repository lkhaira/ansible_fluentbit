# Ansible Fluent-bit role
Simple role to install and setup [Fluent-bit](https://fluentbit.io/)

## Role Variables

Name | Description | Default
--- | --- | --- 
fluentbit_config_path | Path to configuration and parsers file | /etc/fluent-bit
fluentbit_flush | Set the flush time in seconds.nanoseconds. The engine loop uses a Flush timeout to define when is required to flush the records ingested by input plugins through the defined output plugins. | 5
fluentbit_grace | Set the grace time in seconds as Integer value. The engine loop uses a Grace timeout to define wait time on exit | 5
fluentbit_daemon | Boolean value to set if Fluent Bit should run as a Daemon (background) or not. Allowed values are: yes, no, on and off | off
fluentbit_dns_mode | Set the primary transport layer protocol used by the asynchronous DNS resolver which can be overriden on a per plugin basis | UDP
fluentbit_log_file | Absolute path for an optional log file. By default all logs are redirected to the standard error interface (stderr). | 
fluentbit_log_level | Set the logging verbosity level. | info
fluentbit_http_server | Enable built-in HTTP Server | off
fluentbit_http_listen | Set listening interface for HTTP Server when it's enabled | 0.0.0.0
fluentbit_http_port | Set TCP Port for the HTTP Server | 2020
fluentbit_coro_stack_size | Set the coroutines stack size in bytes. The value must be greater than the page size of the running system. Don't set too small value (say 4096), or coroutine threads can overrun the stack buffer. Do not change the default value of this parameter unless you know what you are doing | 24576
fluentbit_scheduler_cap | Set a maximum retry time in second. The property is supported from v1.8.7. | 2000
fluentbit_scheduler_base | Set a base of exponential backoff. The property is supported from v1.8.7. | 5
fluentbit_inputs | An input section defines a source (related to an input plugin) | Name: forward<br>Listen: 0.0.0.0<br>Port: 24224
fluentbit_outputs | The outputs section specify a destination that certain records should follow after a Tag match | Name: srdout<br>Match: '*'

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
