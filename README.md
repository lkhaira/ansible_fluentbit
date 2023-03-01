# Ansible Fluent-bit role
Simple role to install and setup [Fluent-bit](https://fluentbit.io/)

## Role Variables
### Configuration

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

### Pipeline
* `fluentbit_inputs` - list of inputs (sources). Each element of input is collection of key/value dictionary. Default value is:
```yaml
fluentbit_inputs:
  - Name: forward
    Listen: 0.0.0.0
    Port: 24224
```
* `fluentbit_outputs` - list of output (sinks). Each element of output is collection of key/value dictionary. Default value is:
```yaml
fluentbit_outputs:
  - Name: stdout
    Match: '*'
```
* `fluentbit_filters` - list of filters. Each element is collection of key/value dictionary. Defaul value is `[]`. Example:
```yaml
---
- name: Deploy fluent-bit service
  hosts: "{{ lookup('env', 'TARGET') }}"
  become: true
  roles:
    - role: artem_shestakov.fluentbit
      version: "v1.0.0"
  vars:
    fluentbit_inputs:
      - Name: forward
        Listen: 0.0.0.0
        Port: 24224
      - Name: syslog
        Tag: haproxy
        Path: /var/lib/haproxy/dev/log
        Unix_Perm: "0666"
    fluentbit_filters:
      - Name: record_modifier
        Match: "*"
        Record: hostname ${HOSTNAME}
      - Name: parser
        Match: "*"
        Key_Name: data
        Parser: syslog-rfc3164-local
    fluentbit_outputs:
      - Name: es
        Match: *
        Host: 192.168.2.3
        Port: 9200
        Index: my_index
        Type: my_type
    fluentbit_parsers:
      - Name: syslog-rfc3164-local
        Format: regex
        Regex: ^\<(?<pri>[0-9]+)\>(?<time>[^ ]* {1,2}[^ ]* [^ ]*) (?<ident>[a-zA-Z0-9_\/\.\-]*)(?:\[(?<pid>[0-9]+)\])?(?:[^\:]*\:)? *(?<message>.*)$
        Time_Key: time
        Time_Format: '%b %d %H:%M:%S'
        Time_Keep: On
```
* `fluentbit_parsers` - list of parsers. Each element of parser is collection of key/value dictionary. Defaul value is `[]`. Example:
```yaml
fluentbit_parsers:
  - Name: named-capture-test
    Format: regex
    Regex: /^(?<date>[a-zA-Z]+ \d+ \d+\:\d+\:\d+) (?<message>.*)/m
  - Name: docker
    Format: json
    Time_Key: time
    Time_Format: "%Y-%m-%dT%H:%M:%S %z"
```
* `fluentbit_multiline_parsers` - list of multiline parsers. Each element of parser is collection of key/value dictionary. Every parser should contains list of `rules`. Each rule is dictionary of three elements: `state_name`, `regex_pattern` and `next_state`. Defaul value is `[]`. Example:
```yaml
fluentbit_multiline_parsers:
  - name: multiline-regex-test
    type: regex
    flush_timeout: 1000
    rules:
      - state_name: start_state
        regex_pattern: /([a-zA-Z]+ \d+ \d+\:\d+\:\d+)(.*)/
        next_state: cont
      - state_name: cont
        regex_pattern: /^\s+at.*/
        next_state: cont
```


# Example Playbook
```
example here
```

## License
BSD

## Author Information
Artem Shestakov artem.s.shestakov@yandex.ru
