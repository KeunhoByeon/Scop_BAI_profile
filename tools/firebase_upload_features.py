import firebase_admin
import numpy as np
import requests
from firebase_admin import credentials, firestore

class Firebase:
    def __init__(self):
        if not firebase_admin._apps:
            print('Initializing firebase app')
            cred = credentials.Certificate('firebase_key.json')
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.users_ref = self.db.collection(u'photos')
        self.photographer_ref = self.db.collection(u'studioUsers')

    def load_features(self):
        # TODO
        db_images = []
        db_features = []

        for i, photo in enumerate(self.users_ref.stream()):
            if photo.to_dict()['genre'] not in ('50/100', '50일', '100일', '돌', '만삭'):
                continue

            # Image annotation
            photo_id = photo.id
            photo_category = photo.to_dict()['category']
            photo_url = photo.to_dict()['image']
            photo_photographer = photo.to_dict()['photographerId']
            img_anno = {
                'id': photo_id,
                'category': photo_category,
                'url': photo_url,
                'photographerId': photo_photographer,
                'studioName': '',
                'studioImage': ''
            }
            db_images.append(img_anno)

            # Image feature
            photo_feature = photo.to_dict()['feature']
            photo_feature = np.array(photo_feature.split(', ')).astype(np.float)
            db_features.append(photo_feature)

        return np.array(db_images), db_features

    def load_image(self, img_id):
        for doc in self.stream:
            if doc.id == img_id:
                doc = doc.to_dict()
                image_path = doc['image']

firebase = Firebase()