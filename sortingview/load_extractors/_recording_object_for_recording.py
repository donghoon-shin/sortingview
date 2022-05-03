import spikeinterface as si
import spikeinterface.extractors as se
import kachery_client as kc


def _recording_object_for_recording(recording: si.BaseRecording):
    if hasattr(recording, 'sortingview_object'):
        return recording.sortingview_object
    elif isinstance(recording, se.NwbRecordingExtractor):
        file_path = recording._file_path
        electrical_series_name = recording._electrical_series_name
        nwb_file_uri = kc.link_file(file_path)
        recording_object = {
            'recording_format': 'nwb2',
            'data': {
                'nwb_file_uri': nwb_file_uri,
                'electrical_series_name': electrical_series_name
            }
        }
    else:
        raise Exception('Unable to create sortingview object from recording')
    setattr(recording, 'sortingview_object', recording_object)
    return recording_object