import React from "react";
import PropTypes from "prop-types";
import "bootstrap/dist/css/bootstrap.min.css";
import note from "../assets/loading_note.gif"


class Lyrics extends React.Component {
  render() {

    const { artist, song, lyrics, artist_img, album_title, timeLeft, isLoading, songError } = this.props;
    const mainLyrics = (
      <div>
        <p id="songTitle" className="h2">{artist} - {song}</p>
        <div>
            <img className="img-thumbnail" id="artistPic" src={artist_img} alt={"#"}/>
            <img className="img-thumbnail" id="titlePic" src={album_title} alt={"#"}/>
        </div>
        <div className="text-justify">
            <span style={{whiteSpace: "pre-wrap"}}>
              {lyrics}
            </span>
        </div>
      </div>
    )
    const lyricsErrorDetail = songError ? <h1>{songError["info"]}</h1> : null

    const showLyrics = (
      <div className="text-center">
        {songError ? lyricsErrorDetail : mainLyrics}
      </div>
    );

    const loadingMessage = <div className="loading"><img src={note} alt="loading..." /></div>;
    return (
      <div>
        {isLoading ? loadingMessage : showLyrics}
      </div>
        );
    }
}
Lyrics.propTypes = {
  artist: PropTypes.string,
  song: PropTypes.string,
  lyrics: PropTypes.string,
  artist_img: PropTypes.string,
  album_title: PropTypes.string,
  error: PropTypes.string,
};

export default Lyrics;
