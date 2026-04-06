import './app.css'
import { footer } from './myComponents/footerText';
export function App() {
  return (
    <div>
      <h1>Search for a Movie</h1>
      <textarea placeholder="Enter movie name here"></textarea>
      <button type="submit">Search</button>
      {footer()}
    </div>    
  );
}
