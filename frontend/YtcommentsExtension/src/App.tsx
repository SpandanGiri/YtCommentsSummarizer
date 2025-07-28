import { useState } from 'react'
import './App.css'
import api from './api.ts'



function App() {

  const [summary, setSummary] = useState('');

  async function getActiveTabUrl(): Promise<string> {
    return new Promise((resolve, reject) => {
      try {
        chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
          if (tabs[0] && tabs[0].url) {
            resolve(tabs[0].url);
          } else {
            reject("No active tab or URL found");
          }
        });
      } catch (error) {
        reject(error);
      }
    });
  }

  async function sendUrl(){

    try{
      let url = await getActiveTabUrl();
      console.log('sending url to server '+ url);
      const resp = await api.post('/', { content: url });
      console.log(resp.data.summary)
      setSummary(resp.data.summary)
    }catch (error) {
        console.error("Error sending prompt to server", error);
    }
    
  }

  return (
    <>
      <h1>Youtube Comments Summarizert</h1>
      <div className="card">
        <p className="read-the-docs">
          Click to get the summarized response
        </p>
        <button onClick={sendUrl}>URL
        </button>
        <div className='response'>
          {summary}
        </div>
      </div>
    </>
  )
}

export default App
