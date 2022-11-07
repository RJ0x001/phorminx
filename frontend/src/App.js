import React from "react";
// import API from "./utils/API";
import Lyrics from "./lyrics/Lyrics";
import UserInfo from './user/UserInfo'
import Navbar from './navbar/Navbar'
// import xtype from 'xtypejs'
import styles from "./style.css"
// import axios from "axios";
class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      artist: null,
      song: null,
      lyrics: null,
      timeLeft: 1000,
      songError: null,
    };
  };

  render() {
    const { isLoading, artist, song, artist_img, album_title, timeLeft, lyrics, songError } = this.state;
    return (
      <div>
        <Navbar/>
        <Lyrics isLoading={isLoading} artist={artist} song={song} artist_img={artist_img} album_title={album_title}lyrics={lyrics} timeLeft={timeLeft} songError={songError}/>
      </div>
    );
  };


  // todo setinterval with async func
  async componentDidMount() {
         await this.getLyrics();
         try {
           setInterval(this.getLyrics, this.state.timeLeft);
         } catch(e) {
           console.log(e);
         }
   }

  async componentWillUnmount() {
    clearInterval(this.interval);
  }

  getLyrics = async () => {
    // console.log(this.state);
    const res = await fetch('http://localhost:5000/jaskier/lyrics');

    if (!res.ok) {
      const message = `An error has occured: ${res.status}`;
      throw new Error(message);
    }

    const blocks = await res.json();

    const song = blocks.song;
    const artist = blocks.artist;
    const lyrics = blocks.lyrics;
    const artist_img = blocks.artist_img;
    const album_title = blocks.album_title;
    const timeLeft = blocks.next_track * 1000;
    const songError = blocks.song_error;

    this.setState({
       ...this.state, ...{
         isLoading: false,
         song,
         artist,
         artist_img,
         album_title,
         timeLeft,
         lyrics,
         songError
           }
     });
};

}
export default App;
