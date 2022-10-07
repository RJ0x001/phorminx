import React from "react";
import API from "./utils/API";
import Lyrics from "./lyrics/Lyrics";

import styles from "./style.css"
import axios from "axios";
class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      artist: null,
      song: null,
      lyrics: null,
      timeLeft: null,
      songError: null,
      timer: null
    };
  };

  render() {
    const { isLoading, artist, song, artist_img, album_title, timeLeft, lyrics, songError } = this.state;
    return (
        <Lyrics isLoading={isLoading} artist={artist} song={song} artist_img={artist_img} album_title={album_title}
        lyrics={lyrics} timeLeft={timeLeft} songError={songError}/>
    );
  };

  async componentDidMount() {
    this.getData();
    const isLoading = this.state.isLoading;
  };

  async componentWillUnmount() {
    clearInterval(this.interval);
  }

  getData = async () => {

   let lyricsData = await API.get('/');

   const song = lyricsData.data.song
   const artist = lyricsData.data.artist
   const lyrics = lyricsData.data.lyrics
   const artist_img = lyricsData.data.artist_img
   const album_title = lyricsData.data.album_title
   const timeLeft = lyricsData.data.next_track
   const songError = lyricsData.data.song_error

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

   this.interval = setInterval(() => {
     this.getData();
   }, 1000 * this.state.timeLeft);

  };

}
export default App;
