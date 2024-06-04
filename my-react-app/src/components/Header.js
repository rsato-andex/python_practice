import React, { useState, useEffect } from 'react';

const Header = () => {
    const [username, setUsername] = useState('');

    useEffect(() => {
        // Flaskのセッションデータを取得
        fetch('/api/session')
            .then(response => response.json())
            .then(data => setUsername(data.username));
    }, []);

    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    return (
        <header className="bg-gray-100 shadow-md p-2">
            <div className="flex items-center justify-between">
                <a href="/home"><img src="/static/images/MySite.jpg" alt="Logo" className="h-logo" /></a>
                <button className="block lg:hidden px-4 py-2 text-gray-700" onClick={toggleMenu}>
				{{ username }}様
                </button>
                <nav className={`lg:flex ${isMenuOpen ? 'block' : 'hidden'}`}>
                    <ul className="flex flex-col lg:flex-row">
                        <li className="bg-blue-500 rounded mr-4 py-2 px-4">
                            <a href="/user/update" className="text-white hover:text-indigo-500">
                                ユーザー情報の変更
                            </a>
                        </li>
                        <li className="bg-blue-500 rounded mr-4 py-2 px-4">
                            <a href="/logout" className="text-white hover:text-indigo-500">
                                ログアウト
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </header>
    );
};

export default Header;
