import React from "react";
import PropTypes from "prop-types";
import "bootstrap/dist/css/bootstrap.min.css";

class Lyrics extends React.Component {
  render() {
    const { artist, song, lyrics, isLoading } = this.props;
    const lyricsDetails = (
      <div className="text-center">
        <p class="h2">{artist} - {song}</p>
        <span style={{whiteSpace: "pre-wrap"}}>
          {lyrics}
        </span>
      </div>
    );
    const loadingMessage = <div className="text-center">Loading...</div>;
    return (
      <div>
        {isLoading ? loadingMessage : lyricsDetails}
      </div>
        );
    }
}
Lyrics.propTypes = {
  artist: PropTypes.string,
  song: PropTypes.string,
  lyrics: PropTypes.bool
};

export default Lyrics;
