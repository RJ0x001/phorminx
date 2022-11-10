import React from "react";
import PropTypes from "prop-types";
import "bootstrap/dist/css/bootstrap.min.css";
import note from "../assets/loading_note.gif"


class Lyrics extends React.Component {

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
    console.log("state from getLyrics", this.state);
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
    const timeLeft = blocks.next_track == 0 ? 10000  : blocks.next_track * 1000;
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


  render() {
    const mainLyrics = (
      <div>
        <p id="songTitle" className="h2">{this.state.artist} - {this.state.song}</p>
        <div>
            <img className="img-thumbnail" id="artistPic" src={this.state.artist_img} alt={"#"}/>
            <img className="img-thumbnail" id="titlePic" src={this.state.album_title} alt={"#"}/>
        </div>
        <div className="text-justify">
            <span style={{whiteSpace: "pre-wrap"}}>
              {this.state.lyrics}
            </span>
        </div>
      </div>
    )
    const lyricsErrorDetail = this.state.songError ? <h1>{this.state.songError ["info"]}</h1> : null

    const showLyrics = (
      <div className="text-center">
        {this.state.songError ? lyricsErrorDetail : mainLyrics}
      </div>
    );

    const loadingMessage = <div className="loading"><img src={note} alt="loading..." /></div>;
    return (
      <div>
        {this.state.isLoading ? loadingMessage : showLyrics}
      </div>
        );
    }
}

export default Lyrics;
