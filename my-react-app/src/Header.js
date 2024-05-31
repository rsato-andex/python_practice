// src/Header.js
import React, { useState } from 'react';

const Header = ({ username }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="bg-gray-100 shadow-md p-2">
      <div className="flex items-center justify-between">
        <a href="/home"><img src="/static/images/MySite.jpg" alt="Logo" className="h-logo" /></a>
        <nav>
          <ul className="flex">
            <li 
              className="bg-gray-500 text-2xl rounded mr-4 py-2 px-4 cursor-pointer"
              onClick={toggleMenu}
            >
              {username}様
            </li>
            {isMenuOpen && (
              <div className="absolute top-12 right-4 bg-white shadow-lg rounded-lg py-2">
                <ul>
                  <li className="py-2 px-4 hover:bg-gray-200"><a href="/user/update">ユーザー情報の変更</a></li>
                  <li className="py-2 px-4 hover:bg-gray-200"><a href="/logout">ログアウト</a></li>
                </ul>
              </div>
            )}
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;
