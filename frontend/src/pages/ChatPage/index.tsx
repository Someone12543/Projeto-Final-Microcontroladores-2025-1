import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { createTheme } from '@mui/material/styles';
import DashboardIcon from '@mui/icons-material/Dashboard';
import { AppProvider, type Navigation } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import {ChatComponent} from '../../components/ChatComponent'; // Se você exportou como `Chat`

type Message = {
    sender: 'user' | 'printer';
    content: string;
    timestamp: string;
};

const demoTheme = createTheme({
    cssVariables: {
        colorSchemeSelector: 'data-toolpad-color-scheme',
    },
    colorSchemes: { light: true, dark: true },
    breakpoints: {
        values: {
            xs: 0,
            sm: 600,
            md: 600,
            lg: 1200,
            xl: 1536,
        },
    },
});

const NAVIGATION: Navigation = [
    {
        kind: 'header',
        title: 'Histórico',
    },
    {
        title: 'Chat 1',
        icon: <DashboardIcon />,
    },
];

export default function ChatPage() {
    const [log, setLog] = React.useState<Message[]>([]);

    const handleSend = (userMessage: string) => {
        const now = new Date().toISOString();
        setLog((prev) => [
            ...prev,
            { sender: 'user', content: userMessage, timestamp: now },
            {
                sender: 'printer',
                content: `Recebido: "${userMessage}". Processando...`,
                timestamp: now,
            },
        ]);
    };

    return (
        <AppProvider
            navigation={NAVIGATION}
            theme={demoTheme}
            branding={{
                logo: <img alt="" />,
                title: 'IMPRESSORA BRABA :)',
                homeUrl: '/toolpad/core/introduction',
            }}
        >
            <DashboardLayout >
                <ChatComponent id={"001"} chatLog={log} onSend={handleSend} demoTheme={demoTheme} />
            </DashboardLayout>
        </AppProvider>
    );
}