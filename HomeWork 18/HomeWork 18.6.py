import datetime


def log_message(severity, *args, **kwargs):
    
    valid_severities = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        
    timestamp = kwargs.get('timestamp', datetime.datetime.now())


    log_entry = f"[{severity}]"
            
    for message in args:
        log_entry += f" {message}"
                
    if kwargs:
        log_entry += ' | Metadata: ' + ', '.join(f"{key}={value}" for key, value in kwargs.items())

    print(log_entry)


log_message('DEBUG', 'This is a debug message.', timestamp=datetime.datetime.now(), user='dev')
log_message('INFO', 'This is an informational message.', 'Another message.', timestamp=datetime.datetime.now(), user='admin')
log_message('WARNING', 'This is a warning message.', user='admin')
log_message('ERROR', 'This is an error message.', user='admin')
log_message('CRITICAL', 'This is a critical error message.', user='admin')
