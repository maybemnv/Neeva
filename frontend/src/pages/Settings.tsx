import { useAuth } from '@/contexts/AuthContext';
import { User, Bell, Lock, Database, LogOut, Download } from 'lucide-react';
import api from '@/lib/api';

const Settings = () => {
    const { user, logout } = useAuth();

    const handleExportData = async () => {
        try {
            const response = await api.get('/users/me');
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(response.data, null, 2));
            const downloadAnchorNode = document.createElement('a');
            downloadAnchorNode.setAttribute("href", dataStr);
            downloadAnchorNode.setAttribute("download", "neeva_user_data.json");
            document.body.appendChild(downloadAnchorNode);
            downloadAnchorNode.click();
            downloadAnchorNode.remove();
        } catch (error) {
            console.error("Failed to export data", error);
        }
    };

    return (
        <div className="min-h-screen bg-transparent">
            <div className="max-w-4xl mx-auto space-y-8">
                {/* Header */}
                <div className="animate-in">
                    <h1 className="text-4xl md:text-5xl font-serif font-bold text-gray-900 mb-2">Settings</h1>
                    <p className="text-lg text-gray-600">Manage your account and preferences</p>
                </div>

                {/* Profile Section */}
                <div className="glass rounded-[2rem] p-8 shadow-sm animate-in">
                    <div className="flex items-center gap-3 mb-6">
                        <User className="w-5 h-5 text-purple-600" />
                        <h2 className="text-xl font-bold text-gray-900">Profile</h2>
                    </div>
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Name</label>
                            <input
                                type="text"
                                defaultValue={user?.name}
                                className="w-full px-5 py-3 bg-white/50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none text-gray-900"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
                            <input
                                type="email"
                                defaultValue={user?.email}
                                disabled
                                className="w-full px-5 py-3 bg-gray-100 border border-gray-200 rounded-2xl text-gray-500 cursor-not-allowed"
                            />
                        </div>
                    </div>
                </div>

                {/* Notifications */}
                <div className="glass rounded-[2rem] p-8 shadow-sm animate-in">
                    <div className="flex items-center gap-3 mb-6">
                        <Bell className="w-5 h-5 text-amber-600" />
                        <h2 className="text-xl font-bold text-gray-900">Notifications</h2>
                    </div>
                    <div className="space-y-4">
                        {['Daily Check-ins', 'Weekly Summaries', 'Exercise Reminders', 'Community Updates'].map((item) => (
                            <label key={item} className="flex items-center justify-between p-4 bg-white/50 rounded-2xl hover:bg-white/80 transition-colors duration-200 cursor-pointer border border-transparent hover:border-gray-200">
                                <span className="text-gray-900 font-medium">{item}</span>
                                <input type="checkbox" defaultChecked className="w-5 h-5 text-purple-600 rounded focus:ring-purple-500" />
                            </label>
                        ))}
                    </div>
                </div>

                {/* Privacy */}
                <div className="glass rounded-[2rem] p-8 shadow-sm animate-in">
                    <div className="flex items-center gap-3 mb-6">
                        <Lock className="w-5 h-5 text-green-600" />
                        <h2 className="text-xl font-bold text-gray-900">Privacy</h2>
                    </div>
                    <div className="space-y-4">
                        {['Anonymous Mode', 'Analytics', 'Data Sharing'].map((item) => (
                            <label key={item} className="flex items-center justify-between p-4 bg-white/50 rounded-2xl hover:bg-white/80 transition-colors duration-200 cursor-pointer border border-transparent hover:border-gray-200">
                                <span className="text-gray-900 font-medium">{item}</span>
                                <input type="checkbox" className="w-5 h-5 text-purple-600 rounded focus:ring-purple-500" />
                            </label>
                        ))}
                    </div>
                </div>

                {/* Data & Account */}
                <div className="glass rounded-[2rem] p-8 shadow-sm animate-in">
                    <div className="flex items-center gap-3 mb-6">
                        <Database className="w-5 h-5 text-gray-600" />
                        <h2 className="text-xl font-bold text-gray-900">Data & Account</h2>
                    </div>
                    <div className="space-y-3">
                        <button
                            onClick={handleExportData}
                            className="w-full flex items-center justify-between px-5 py-4 bg-white/50 text-gray-700 rounded-2xl hover:bg-white/80 font-medium transition-colors duration-200 border border-transparent hover:border-gray-200"
                        >
                            <span>Export My Data</span>
                            <Download size={18} />
                        </button>
                        <button className="w-full text-left px-5 py-4 bg-white/50 text-gray-700 rounded-2xl hover:bg-white/80 font-medium transition-colors duration-200 border border-transparent hover:border-gray-200">
                            Clear All Mood Data
                        </button>
                        <button className="w-full text-left px-5 py-4 bg-white/50 text-gray-700 rounded-2xl hover:bg-white/80 font-medium transition-colors duration-200 border border-transparent hover:border-gray-200">
                            Clear Chat History
                        </button>
                        <button
                            onClick={logout}
                            className="w-full flex items-center justify-center gap-2 px-5 py-4 bg-orange-50 text-orange-600 rounded-2xl hover:bg-orange-100 font-medium transition-colors duration-200"
                        >
                            <LogOut size={18} />
                            Logout
                        </button>
                        <button className="w-full text-left px-5 py-4 bg-red-50 text-red-600 rounded-2xl hover:bg-red-100 font-medium transition-colors duration-200">
                            Delete Account
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Settings;
