import React from 'react';
import './App.css';
import Header from './Header';

function App() {
  const username = 'ユーザー名'; // 必要に応じて、適切なセッション管理を追加

  return (
    <div className="App">
      <Header username={username} />
      <div className="content">
        <h1>メインコンテンツ</h1>
      </div>
    </div>
  );
}

export default App;
