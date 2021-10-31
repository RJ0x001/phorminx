import React from "react";
import API from "./utils/API";
import Lyrics from "./lyrics/Lyrics";

import styles from "./style.css"

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      artist: null,
      song: null,
      lyrics: null,
      timeLeft: null,
    };
  }

  render() {
    const { isLoading, artist, song, artist_img, album_title, timeLeft, lyrics } = this.state;
    return (
        <Lyrics isLoading={isLoading} artist={artist} song={song} artist_img={artist_img} album_title={album_title}
        lyrics={lyrics} timeLeft={timeLeft}/>
    );
  }
  
  async componentDidMount() {

    let lyricsData = await API.get('/');
    const song = lyricsData.data.song
    const artist = lyricsData.data.artist
    const lyrics = lyricsData.data.lyrics
    const artist_img = lyricsData.data.artist_img
    const album_title = lyricsData.data.album_title
    const timeLeft = lyricsData.data.timeLeft

    this.setState({
      ...this.state, ...{
        isLoading: false,
        song,
        artist,
        artist_img,
        album_title,
        timeLeft,
        lyrics,
          }
    });
 };
}
export default App;
