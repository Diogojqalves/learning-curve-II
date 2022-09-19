import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore'; //database
import 'firebase/compat/auth'; //authentication

const config = {
    apiKey: "AIzaSyAb1WxXVFWMGbjthBrnPxgCXJTIeRjIRFE",
    authDomain: "e-store-165d6.firebaseapp.com",
    projectId: "e-store-165d6",
    storageBucket: "e-store-165d6.appspot.com",
    messagingSenderId: "385879240794",
    appId: "1:385879240794:web:b92c94d8dc6805240a6863",
    measurementId: "G-S6Y7SED341"
  };

//store User Data
export const createUserProfileDocument = async (userAuth, additionalData) => {
  if(!userAuth) return;

  const userRef = firestore.doc(`users/${userAuth.uid}`)
  const snapShot = await userRef.get(); //firestore query

  //if user doesn´t exist
  if(!snapShot.exist) {
      const {displayName, email} = userAuth;
      const createAt = new Date();
    // create snapShot
      try {
        await userRef.set({
          displayName,
          email,
          createAt,
          ...additionalData
        })
      } catch (error) {
        console.log('error creating user', error.message);
      }
    }
    return userRef;
}

firebase.initializeApp(config);

//use google auth

export const auth = firebase.auth();
export const firestore = firebase.firestore();

const provider = new firebase.auth.GoogleAuthProvider();
provider.setCustomParameters({promp: 'select_account'}); //trigger google pop-up

export const signInWithGoogle = () => auth.signInWithPopup(provider);

export default firebase;