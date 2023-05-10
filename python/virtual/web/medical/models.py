from django.db import models

PROCESS_STATUS =(

    (1,'Pending'),
    (2,'Executed'),
    )
RETURN_STATUS =(

    (1,'Pending'),
    (2,'Success'),
    (3,'Failed'),
    )
CALL_BACK_STATUS =(
    (1,'Pending'),
    (2,'Executed'),
)

class process_queue(models.Model):
    process_id                  =    models.IntegerField(help_text='PK NN')
    title                       =    models.CharField(max_length=200,help_text='NN')
    process_file_location       =    models.TextField(help_text='NN')
    process_status              =    models.IntegerField(choices=PROCESS_STATUS,default=1)
    return_status               =    models.IntegerField(choices=RETURN_STATUS,default=1)
    return_json                 =    models.TextField()
    call_back_url               =    models.CharField(max_length=200)
    call_back_status            =    models.IntegerField(choices=CALL_BACK_STATUS,default=1)
    call_back_json              =    models.TextField()
    process_entry_date          =    models.DateTimeField()

    #def __str__(self) -> str:
        