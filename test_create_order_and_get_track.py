import sender_stand_request
import data

def test_get_order_track():
    response_track = sender_stand_request.post_new_order(data.order_body)
    track = response_track.json()['track']
    response = sender_stand_request.get_order_from_track(track)
    assert response.status_code == 200
    print (response.status_code)

test_get_order_track()

# Алиса Корнюшина, 27-я когорта — Финальный проект. Инженер по тестированию плюс