from ferrisapp.app.services.ferris_events import FerrisEvents


FerrisEvents().send(
    event_type="ferris_executor.run_execution.triggered_run",
    event_source="testsrc",
    data={"evt_data": "payload"},
    reference_id="someide1308",
    topic="newtopic"
)

