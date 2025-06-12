import {useSendMessage, useGetChats} from "./requests.ts";

export const useChatAPI = () =>{
    const {
        getChat,
        isLoading: getChatLoading,
        data: getChatData
    } = useGetChats();

    const {
        sendMessage,
        isLoading: sendMessageLoading,
        data: sendMessageData,
    } = useSendMessage();

    return{
        getChat: {
            query: getChat,
            isLoading: getChatLoading,
            data: getChatData,
        },
        sendMessage: {
            query: sendMessage,
            isLoading: sendMessageLoading,
            data: sendMessageData,
        }
    }

}
