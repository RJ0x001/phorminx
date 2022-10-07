import axios from "axios";
import qs from 'qs';

export default axios.create({
  baseURL: "http://localhost:5000/jaskier/lyrics",
  responseType: "json",
});

export const BASENAME = '';
