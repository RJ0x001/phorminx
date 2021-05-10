//
////import './App.css';
//import React, { useEffect, useState } from 'react';
//import axios from 'axios'
//
//function App() {
//  const [isLoading, setLoading] = useState(true);
//  const [getMessage, setMessage] = useState();
//
//  const url = "http://localhost:5000/jaskier/lyrics";
//
//  useEffect(() => {
//    axios.get(url).then(response => {
//      setMessage(response.data);
//      setLoading(false);
//    });
//  }, []);
//
//  if (isLoading) {
//    return <div className="App">Loading...</div>;
//  }
//
//  return (
//    <div className="App">
//      <header className="App-header">
//        <div>
//           {getMessage.artist} - {getMessage.song}
//        </div>
//        <div>
//            {getMessage.lyrics.split("\n").map((i,key) => {
//            return <div key={key}>{i}</div>;
//        })}
//        </div>
//      </header>
//    </div>
//  );
//}
//
//export default App;

import React from "react";
import API from "./utils/API";
import Lyrics from "./lyrics/Lyrics";


class App extends React.Component {
  interval = 6000;

  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      artist: null,
      song: null,
      lyrics: null
    };
  }
  render() {
    const { isLoading, artist, song, lyrics } = this.state;
    return (
        <Lyrics isLoading={isLoading} artist={artist} song={song} lyrics={lyrics} />
    );
  }
  
  async componentDidMount() {


    let lyricsData = await API.get('/');
    const song = lyricsData.data.song
    const artist = lyricsData.data.artist
    const lyrics = lyricsData.data.lyrics



    console.log(this.interval);

    this.setState({
      ...this.state, ...{
        isLoading: false,
        song,
        artist,
        lyrics
          }
    });
 }}
export default App;
